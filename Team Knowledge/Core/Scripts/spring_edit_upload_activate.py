#!/opt/n8n/venv/bin/python3
"""
spring_edit_upload_activate.py
Stap 1: upload productafbeeldingen via staged uploads naar Shopify
Stap 2: producten activeren (DRAFT → ACTIVE)
Stap 3: smoke test — verifieer producten, pagina en collection
"""

import sys
import json
import urllib.request
import urllib.error

sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/shopify')
from shopify_handler import ShopifyClient
from connection import STORE, API_VERSION, _get_token

PRODUCTS = [
    {"id": "10781811278166", "image_path": "/opt/myPKA/Team Inbox/top.jpg",   "alt": "Spring Look 1 — Top"},
    {"id": "10781811605846", "image_path": "/opt/myPKA/Team Inbox/layer.jpg", "alt": "Spring Look 1 — Layer"},
    {"id": "10781811671382", "image_path": "/opt/myPKA/Team Inbox/pants.jpg", "alt": "Spring Look 1 — Pants"},
]

def graphql_direct(token, query, variables=None):
    """GraphQL call via raw urllib (geen interactie)."""
    url = f"https://{STORE}/admin/api/{API_VERSION}/graphql.json"
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": token,
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    if "errors" in result:
        raise RuntimeError(f"GraphQL errors: {result['errors']}")
    return result


def staged_upload(token, image_path, filename, mime_type="image/jpeg"):
    """Stap A: vraag staged upload URL op."""
    mutation = """
    mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
      stagedUploadsCreate(input: $input) {
        stagedTargets {
          url
          resourceUrl
          parameters { name value }
        }
        userErrors { field message }
      }
    }
    """
    variables = {
        "input": [{
            "filename": filename,
            "mimeType": mime_type,
            "resource": "IMAGE",
            "fileSize": str(__import__('os').path.getsize(image_path)),
            "httpMethod": "PUT",
        }]
    }
    result = graphql_direct(token, mutation, variables)
    errors = result["data"]["stagedUploadsCreate"]["userErrors"]
    if errors:
        raise RuntimeError(f"Staged upload error: {errors}")
    target = result["data"]["stagedUploadsCreate"]["stagedTargets"][0]
    return target["url"], target["resourceUrl"], target["parameters"]


def put_file_to_staged_url(upload_url, image_path, parameters, mime_type="image/jpeg"):
    """Stap B: upload het bestand naar de staged URL via PUT."""
    with open(image_path, "rb") as f:
        data = f.read()

    req = urllib.request.Request(
        upload_url,
        data=data,
        headers={"Content-Type": mime_type},
        method="PUT",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"PUT naar staged URL mislukt ({e.code}): {e.read().decode()}")
    return status


def attach_image_to_product(token, product_id, resource_url, alt):
    """Stap C: koppel de geüploade afbeelding aan het product."""
    import time
    mutation = """
    mutation productCreateMedia($productId: ID!, $media: [CreateMediaInput!]!) {
      productCreateMedia(productId: $productId, media: $media) {
        media {
          ... on MediaImage {
            id
            image { url }
          }
        }
        mediaUserErrors { field message }
      }
    }
    """
    variables = {
        "productId": f"gid://shopify/Product/{product_id}",
        "media": [{
            "mediaContentType": "IMAGE",
            "originalSource": resource_url,
            "alt": alt,
        }]
    }
    result = graphql_direct(token, mutation, variables)
    print(f"    C-raw: {json.dumps(result.get('data', {}), indent=2)[:400]}")
    errors = result["data"]["productCreateMedia"]["mediaUserErrors"]
    if errors:
        raise RuntimeError(f"productCreateMedia error: {errors}")
    media = result["data"]["productCreateMedia"]["media"]
    # Media processing is async — wait and check via product fetch
    time.sleep(3)
    if media:
        first = media[0]
        if first is not None and isinstance(first, dict):
            img = first.get("image")
            if img:
                return img.get("url", resource_url)
    # Fallback: return resource_url, image may still be processing
    return resource_url


def activate_product(token, product_id):
    """Activeer een product (DRAFT → ACTIVE)."""
    mutation = """
    mutation productUpdate($input: ProductInput!) {
      productUpdate(input: $input) {
        product { id title status }
        userErrors { field message }
      }
    }
    """
    variables = {
        "input": {
            "id": f"gid://shopify/Product/{product_id}",
            "status": "ACTIVE",
        }
    }
    result = graphql_direct(token, mutation, variables)
    errors = result["data"]["productUpdate"]["userErrors"]
    if errors:
        raise RuntimeError(f"productUpdate error: {errors}")
    return result["data"]["productUpdate"]["product"]


def main():
    token = _get_token()
    client = ShopifyClient()

    print("=" * 60)
    print("STAP 1 — Afbeeldingen uploaden en koppelen")
    print("=" * 60)

    image_results = {}
    for p in PRODUCTS:
        pid = p["id"]
        img_path = p["image_path"]
        alt = p["alt"]
        filename = img_path.split("/")[-1]
        print(f"\n  Verwerken: {alt} ({filename})")

        try:
            # A: Staged upload URL ophalen
            upload_url, resource_url, parameters = staged_upload(token, img_path, filename)
            print(f"    A. Staged URL verkregen")

            # B: Bestand uploaden
            status = put_file_to_staged_url(upload_url, img_path, parameters)
            print(f"    B. PUT geslaagd (HTTP {status})")

            # C: Koppelen aan product
            img_url = attach_image_to_product(token, pid, resource_url, alt)
            print(f"    C. Gekoppeld: {img_url[:80]}...")
            image_results[pid] = {"status": "OK", "url": img_url}

        except Exception as e:
            print(f"    FOUT: {e}")
            image_results[pid] = {"status": "FOUT", "error": str(e)}

    print("\n" + "=" * 60)
    print("STAP 2 — Producten activeren (DRAFT → ACTIVE)")
    print("=" * 60)

    activate_results = {}
    for p in PRODUCTS:
        pid = p["id"]
        try:
            prod = activate_product(token, pid)
            status = prod.get("status", "?")
            title = prod.get("title", pid)
            print(f"  {title}: {status}")
            activate_results[pid] = {"status": status}
        except Exception as e:
            print(f"  Product {pid}: FOUT — {e}")
            activate_results[pid] = {"status": "FOUT", "error": str(e)}

    print("\n" + "=" * 60)
    print("STAP 3 — Smoke test")
    print("=" * 60)

    # Check producten
    print("\n  [Producten]")
    product_checks = {}
    for p in PRODUCTS:
        pid = p["id"]
        try:
            prod = client.product(pid)
            status_ok = prod["status"].upper() == "ACTIVE"
            img_ok = len(prod.get("images", [])) > 0
            icon_s = "✓" if status_ok else "✗"
            icon_i = "✓" if img_ok else "✗"
            print(f"  {icon_s} status=ACTIVE  {icon_i} image aanwezig  — {prod['title']}")
            product_checks[pid] = {"status_ok": status_ok, "img_ok": img_ok}
        except Exception as e:
            print(f"  ✗ Product {pid}: FOUT — {e}")
            product_checks[pid] = {"status_ok": False, "img_ok": False}

    # Check pagina
    print("\n  [Spring Edit pagina]")
    page_ok = False
    try:
        page = client.page(handle='the-spring-edit')
        body_len = len(page.get("body_html") or "")
        tmpl = page.get("template_suffix") or "(geen)"
        page_ok = body_len > 0
        icon_p = "✓" if page_ok else "✗"
        print(f"  {icon_p} Pagina: '{page['title']}' | template: {tmpl} | body: {body_len} tekens")
        page_url = f"https://{STORE}/pages/{page['handle']}"
        print(f"     URL: {page_url}")
    except Exception as e:
        print(f"  ✗ Pagina ophalen mislukt: {e}")
        page_url = f"https://{STORE}/pages/the-spring-edit"

    # Check collection
    print("\n  [Collection: the-spring-edit-look-i]")
    coll_ok = False
    try:
        coll_query = """
        {
          collectionByHandle(handle: "the-spring-edit-look-i") {
            title
            productsCount { count }
            products(first: 5) {
              nodes { title status }
            }
          }
        }
        """
        coll_result = client.graphql(coll_query)
        coll = coll_result.get("data", {}).get("collectionByHandle")
        if coll:
            count = coll.get("productsCount", {}).get("count", 0)
            coll_ok = count == 3
            icon_c = "✓" if coll_ok else "✗"
            print(f"  {icon_c} Collection: '{coll['title']}' | {count} producten")
            for node in coll.get("products", {}).get("nodes", []):
                print(f"     - [{node['status']}] {node['title']}")
        else:
            print("  ✗ Collection 'the-spring-edit-look-i' niet gevonden")
    except Exception as e:
        print(f"  ✗ Collection check mislukt: {e}")

    # Samenvatting
    print("\n" + "=" * 60)
    print("SMOKE TEST SAMENVATTING")
    print("=" * 60)
    all_status_ok = all(v["status_ok"] for v in product_checks.values())
    all_img_ok    = all(v["img_ok"] for v in product_checks.values())
    print(f"  {'✓' if all_status_ok else '✗'} Alle 3 producten ACTIVE")
    print(f"  {'✓' if all_img_ok    else '✗'} Alle 3 producten hebben een afbeelding")
    print(f"  {'✓' if page_ok       else '✗'} Spring Edit pagina bereikbaar")
    print(f"  {'✓' if coll_ok       else '✗'} Collection bevat 3 producten")
    print(f"\n  Spring Edit URL: {page_url}")
    print("=" * 60)


if __name__ == "__main__":
    main()
