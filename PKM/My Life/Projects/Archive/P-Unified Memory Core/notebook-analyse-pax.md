# Notebook Analyse: Memory & Context Engineering for Agents
**Bron:** https://raw.githubusercontent.com/oracle-devrel/oracle-ai-developer-hub/main/notebooks/memory_context_engineering_agents.ipynb
**Datum:** 2026-05-20
**Analist:** Pax

---

## TL;DR

Het notebook implementeert een volledig `MemoryManager` met zes geheugentypen op Oracle Database + vector opslag. De kernpatronen (tool output offloading, JIT summary expansion, entity extraction, conversational summarization) zijn direct bruikbaar op onze PostgreSQL 16 + pgvector stack. Oracle-specifieke onderdelen zijn beperkt tot de databaseconnectie en vector store adapter -- de logica zelf is database-agnostisch.

---

## 1. Embedding aanmaken en opslaan

### Wat het doet
Het notebook gebruikt `sentence-transformers/paraphrase-mpnet-base-v2` via `HuggingFaceEmbeddings` uit LangChain. Embeddings worden aangemaakt bij het wegschrijven van tekst naar de vector store -- niet handmatig.

### Oracle-implementatie (notebook)
```python
from langchain_oracledb.vectorstores import OracleVS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import DistanceStrategy

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-mpnet-base-v2"
)

vector_store = OracleVS(
    client=vector_conn,
    embedding_function=embedding_model,
    table_name="VECTOR_SEARCH_DEMO",
    distance_strategy=DistanceStrategy.COSINE,
)

# Embeddings worden automatisch aangemaakt bij add_texts:
vector_store.add_texts(texts=["tekst"], metadatas=[{"key": "val"}])
```

### Vertaling naar onze stack (psycopg2 + pgvector)
Wij gebruiken `all-MiniLM-L6-v2` (sneller, kleiner -- 384 dims vs 768). Embeddings maken we direct aan met `sentence-transformers` en slaan ze op via psycopg2.

```python
from sentence_transformers import SentenceTransformer
import psycopg2
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store(conn, table: str, text: str, metadata: dict):
    """Maak embedding en sla op in pgvector tabel."""
    embedding = model.encode(text).tolist()
    with conn.cursor() as cur:
        cur.execute(f"""
            INSERT INTO {table} (content, embedding, metadata, created_at)
            VALUES (%s, %s::vector, %s, NOW())
            RETURNING id
        """, (text, json.dumps(embedding), json.dumps(metadata)))
        return cur.fetchone()[0]
    conn.commit()

def vector_search(conn, table: str, query: str, k: int = 5, filter_sql: str = None):
    """Semantisch zoeken met cosine similarity."""
    embedding = model.encode(query).tolist()
    where = f"AND {filter_sql}" if filter_sql else ""
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT id, content, metadata,
                   1 - (embedding <=> %s::vector) AS score
            FROM {table}
            WHERE 1=1 {where}
            ORDER BY embedding <=> %s::vector
            LIMIT %s
        """, (json.dumps(embedding), json.dumps(embedding), k))
        return cur.fetchall()
```

**Tabelstructuur voor pgvector:**
```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE memory_vectors (
    id          UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    memory_type TEXT NOT NULL,  -- 'knowledge_base', 'workflow', 'entity', etc.
    content     TEXT NOT NULL,
    embedding   vector(384),    -- all-MiniLM-L6-v2 = 384 dims
    metadata    JSONB,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX ON memory_vectors USING hnsw (embedding vector_cosine_ops);
CREATE INDEX ON memory_vectors (memory_type);
```

**Direct bruikbaar:** Ja -- model en logica zijn identiek, alleen de adapter verschilt.

---

## 2. Tool Output Offloading

### Wat het doet
Wanneer een agent een tool aanroept, kan de output groot zijn (bijv. zoekresultaten, API-responses). In plaats van de volledige output in de context window te zetten, slaat het systeem de output op in een `TOOL_LOG` tabel en geeft de agent alleen een compacte referentie terug. Dit voorkomt context overflow.

### Oracle-implementatie (notebook)
```python
def write_tool_log(self, thread_id, tool_call_id, tool_name, tool_args, tool_output):
    """Log een tool output naar de database en return een compacte referentie."""
    with self.conn.cursor() as cur:
        id_var = cur.var(str)
        cur.execute(f"""
            INSERT INTO {self.tool_log_table}
            (thread_id, tool_call_id, tool_name, tool_args, tool_output)
            VALUES (:thread_id, :tool_call_id, :tool_name, :tool_args, :tool_output)
            RETURNING id INTO :id
        """, {
            "thread_id": str(thread_id), "tool_call_id": tool_call_id,
            "tool_name": tool_name, "tool_args": tool_args,
            "tool_output": tool_output, "id": id_var
        })
        log_id = id_var.getvalue()[0]
    self.conn.commit()

    # Return compacte referentie -- niet de volledige output
    preview = tool_output[:150].replace("\n", " ")
    return f"[Tool Log {log_id}] {tool_name} uitgevoerd. Preview: {preview}..."
```

### Vertaling naar onze stack
```python
def write_tool_log(conn, thread_id: str, tool_call_id: str,
                   tool_name: str, tool_args: str, tool_output: str) -> str:
    """Sla tool output op in PostgreSQL en return compacte referentie."""
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO tool_log
            (thread_id, tool_call_id, tool_name, tool_args, tool_output, created_at)
            VALUES (%s, %s, %s, %s, %s, NOW())
            RETURNING id
        """, (thread_id, tool_call_id, tool_name, tool_args, tool_output))
        log_id = cur.fetchone()[0]
    conn.commit()

    preview = tool_output[:150].replace("\n", " ")
    return f"[Tool Log {log_id}] {tool_name} uitgevoerd. Preview: {preview}..."

def read_tool_log(conn, log_id: str) -> str:
    """Haal volledige tool output op via log ID."""
    with conn.cursor() as cur:
        cur.execute("SELECT tool_output FROM tool_log WHERE id = %s", (log_id,))
        row = cur.fetchone()
    return row[0] if row else f"Tool log {log_id} niet gevonden."
```

**Tabelstructuur:**
```sql
CREATE TABLE tool_log (
    id          UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    thread_id   TEXT NOT NULL,
    tool_call_id TEXT NOT NULL,
    tool_name   TEXT NOT NULL,
    tool_args   TEXT,
    tool_output TEXT,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX ON tool_log (thread_id);
```

**Relevantie voor myPKA:** Direct bruikbaar. Onze Claude Code agents produceren regelmatig grote tool outputs (database queries, bestandsinhoud). Dit patroon houdt de context window schoon.

---

## 3. JIT Summary Expansion

### Wat het doet
Oudere conversatieberichten worden samengevat en gecomprimeerd. De samenvatting krijgt een ID. In de context window staat alleen het ID + een korte beschrijving. Wanneer de agent specifieke details nodig heeft, roept hij `expand_summary(summary_id)` aan -- Just-In-Time. Niet alle samenvattingen worden uitgevouwen, alleen de relevante.

### Twee-staps patroon (notebook)

**Stap 1: Samenvatten en comprimeren**
```python
def summarise_context_window(content: str, memory_manager, llm_client) -> dict:
    """Vat context window samen en sla op in summary memory."""
    summary_prompt = f"""
Je comprimeert een AI agent context window voor latere retrieval.
Produceer een compacte samenvatting met:
- gebruikersdoel en constraints
- vastgestelde feiten/bevindingen
- belangrijke entiteiten
- onopgeloste vragen en volgende acties

Output 4-7 korte bullets. Voeg geen nieuwe feiten toe.

Context window inhoud:
{content[:3000]}
""".strip()

    response = llm_client.chat.completions.create(...)
    summary = response.choices[0].message.content
    summary_id = str(uuid.uuid4())[:8]
    memory_manager.write_summary(summary_id, content, summary, description)
    return {"id": summary_id, "description": description, "summary": summary}

def offload_to_summary(context: str, memory_manager, llm_client,
                       threshold_percent: float = 80.0) -> tuple:
    """Als context > threshold, vat samen en return compacte versie."""
    usage = calculate_context_usage(context)  # tokens / max_tokens * 100
    if usage['percent'] < threshold_percent:
        return context, []

    result = summarise_context_window(context, memory_manager, llm_client)
    compact = f"[Summary ID: {result['id']}] {result['description']}"
    return compact, [result]
```

**Stap 2: JIT expansie wanneer nodig**
```python
def read_summary_memory(self, summary_id: str) -> str:
    """Haal specifieke samenvatting op via ID (just-in-time retrieval)."""
    results = self.summary_vs.similarity_search(
        summary_id, k=5, filter={"id": summary_id}
    )
    if not results:
        return f"Summary {summary_id} niet gevonden."
    return results[0].metadata.get('summary', 'Geen inhoud.')

def read_summary_context(self, query: str = "", k: int = 10) -> str:
    """Context window vult zich ALLEEN met ID + beschrijving -- nooit volledige content."""
    # Geeft een lijst van pointers, niet de volledige samenvattingen
    lines = ["## Summary Memory", "### Roep expand_summary(id) aan voor details.", ""]
    for doc in results:
        lines.append(f"  - [ID: {doc.metadata['id']}] {doc.metadata['description']}")
    return "\n".join(lines)
```

### Vertaling naar onze stack
```python
def write_summary(conn, full_content: str, summary: str,
                  description: str) -> str:
    """Sla samenvatting op in PostgreSQL summary tabel."""
    summary_id = str(uuid.uuid4())[:8]
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO memory_summaries
            (id, full_content, summary, description, created_at)
            VALUES (%s, %s, %s, %s, NOW())
        """, (summary_id, full_content, summary, description))
    conn.commit()
    return summary_id

def expand_summary(conn, summary_id: str) -> str:
    """JIT expansie: haal volledige summary op via ID."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT summary, full_content FROM memory_summaries WHERE id = %s
        """, (summary_id,))
        row = cur.fetchone()
    if not row:
        return f"Summary {summary_id} niet gevonden."
    return row[0]  # of row[1] voor volledige originele content

def get_summary_pointers(conn, limit: int = 10) -> str:
    """Geeft alleen ID + beschrijving voor context window."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, description FROM memory_summaries
            ORDER BY created_at DESC LIMIT %s
        """, (limit,))
        rows = cur.fetchall()
    lines = ["## Summary Memory (pointers -- roep expand_summary(id) aan voor details)"]
    for sid, desc in rows:
        lines.append(f"  - [ID: {sid}] {desc}")
    return "\n".join(lines)
```

**Relevantie voor myPKA:** Dit is precies wat we nodig hebben voor lange sessies. Oude context wordt gecomprimeerd maar blijft opvraagbaar. Claude Code kan `expand_summary` als tool aanroepen.

---

## 4. Entity Extraction

### Wat het doet
Het notebook gebruikt een LLM-call (niet een apart NLP-model) om entiteiten uit tekst te extraheren: personen, plaatsen, systemen. De extractie is JSON-gebaseerd en breed inzetbaar.

### Notebook implementatie
```python
def extract_entities(self, text: str, llm_client) -> list[dict]:
    """Gebruik LLM om entiteiten te extraheren uit tekst."""
    prompt = f'''Extraheer entiteiten uit: "{text[:500]}"
Return JSON: [{{"name": "X", "type": "PERSON|PLACE|SYSTEM", "description": "brief"}}]
Als geen entiteiten: []'''

    response = llm_client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=300
    )
    result = response.choices[0].message.content.strip()

    # Robuuste JSON parsing -- pakt alleen het array gedeelte
    start, end = result.find("["), result.rfind("]")
    if start == -1 or end == -1:
        return []

    parsed = json.loads(result[start:end+1])
    return [
        {"name": e["name"], "type": e.get("type", "UNKNOWN"),
         "description": e.get("description", "")}
        for e in parsed if isinstance(e, dict) and e.get("name")
    ]
```

**Methode:** LLM-based (geen spaCy, geen NER-model). Eenvoudig, flexibel, geen extra dependencies.

### Vertaling naar onze stack
Wij vervangen `gpt-5` door Claude via de Anthropic SDK, of we gebruiken dezelfde structuur maar roepen de Claude Code harness aan.

```python
import anthropic
import json

client = anthropic.Anthropic()

def extract_entities_claude(text: str) -> list[dict]:
    """Extraheer entiteiten via Claude -- geen apart NER-model nodig."""
    prompt = f'''Extraheer entiteiten uit deze tekst: "{text[:500]}"
Return ALLEEN een JSON array: [{{"name": "X", "type": "PERSON|PLACE|SYSTEM|PROJECT", "description": "kort"}}]
Als geen entiteiten gevonden: []'''

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    result = message.content[0].text.strip()

    start, end = result.find("["), result.rfind("]")
    if start == -1 or end == -1:
        return []

    try:
        parsed = json.loads(result[start:end+1])
        return [
            {"name": e["name"], "type": e.get("type", "UNKNOWN"),
             "description": e.get("description", "")}
            for e in parsed if isinstance(e, dict) and e.get("name")
        ]
    except json.JSONDecodeError:
        return []

def write_entity(conn, entities: list[dict]):
    """Sla entiteiten op als vectoren voor semantisch zoeken."""
    for entity in entities:
        text = f"{entity['name']} ({entity['type']}): {entity['description']}"
        embed_and_store(conn, "memory_vectors",
                       text=text,
                       metadata={**entity, "memory_type": "entity"})
```

**Relevantie voor myPKA:** Bruikbaar voor CRM-extractie vanuit journaalentries en sessielogs. Penn kan dit inzetten om personen, projecten en organisaties automatisch te borgen.

---

## 5. Conversational Summarization (compactie van conversatiegeschiedenis)

### Wat het doet
Wanneer een conversatiethread te lang wordt, worden oude berichten gemarkeerd als `summarized` en vervangen door een summary pointer. De berichten blijven in de database maar worden niet meer geladen in de actieve context.

### Notebook implementatie
```python
def mark_as_summarized(self, thread_id: str, summary_id: str,
                       message_ids: list[str] | None = None):
    """Markeer berichten als gesummariseerd -- worden niet meer geladen in actieve context."""
    with self.conn.cursor() as cur:
        if message_ids:
            cur.executemany("""
                UPDATE conversational_memory
                SET summary_id = :summary_id
                WHERE thread_id = :thread_id AND id = :id AND summary_id IS NULL
            """, [{"summary_id": summary_id, "thread_id": thread_id, "id": mid}
                  for mid in message_ids])
        else:
            cur.execute("""
                UPDATE conversational_memory
                SET summary_id = :summary_id
                WHERE thread_id = :thread_id AND summary_id IS NULL
            """, {"summary_id": summary_id, "thread_id": thread_id})

def get_unsummarized_messages(self, thread_id: str, limit: int = 100) -> list[dict]:
    """Return ALLEEN ongesummariseerde berichten -- gesummariseerde worden automatisch uitgesloten."""
    cur.execute("""
        SELECT id, role, content, timestamp
        FROM conversational_memory
        WHERE thread_id = :thread_id AND summary_id IS NULL
        ORDER BY timestamp ASC FETCH FIRST :limit ROWS ONLY
    """, {"thread_id": thread_id, "limit": limit})
```

### Vertaling naar onze stack
```python
def get_unsummarized_messages(conn, thread_id: str, limit: int = 100) -> list[dict]:
    """Haal ongesummariseerde berichten op."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, role, content, created_at
            FROM conversational_memory
            WHERE thread_id = %s AND summary_id IS NULL
            ORDER BY created_at ASC
            LIMIT %s
        """, (thread_id, limit))
        rows = cur.fetchall()
    return [{"id": r[0], "role": r[1], "content": r[2], "timestamp": r[3]}
            for r in rows]

def mark_as_summarized(conn, thread_id: str, summary_id: str,
                       message_ids: list[str] = None):
    """Markeer berichten als gesummariseerd."""
    with conn.cursor() as cur:
        if message_ids:
            for mid in message_ids:
                cur.execute("""
                    UPDATE conversational_memory
                    SET summary_id = %s
                    WHERE thread_id = %s AND id = %s AND summary_id IS NULL
                """, (summary_id, thread_id, mid))
        else:
            cur.execute("""
                UPDATE conversational_memory
                SET summary_id = %s
                WHERE thread_id = %s AND summary_id IS NULL
            """, (summary_id, thread_id))
    conn.commit()
```

---

## 6. Oracle-specifiek vs. PostgreSQL equivalent

| Onderdeel | Oracle (notebook) | PostgreSQL equivalent |
|-----------|-------------------|----------------------|
| Connectie | `oracledb.connect()` | `psycopg2.connect()` |
| Vector store adapter | `langchain_oracledb.OracleVS` | `langchain_postgres.PGVector` of directe psycopg2 |
| HNSW index | `create_index(..., idx_type="HNSW")` | `CREATE INDEX USING hnsw (embedding vector_cosine_ops)` |
| UUID generatie | `SYS_GUID()` | `gen_random_uuid()` |
| RETURNING syntax | `RETURNING id INTO :id` (via cursor.var) | `RETURNING id` + `cursor.fetchone()` |
| Paginering | `FETCH FIRST n ROWS ONLY` | `LIMIT n` |
| Foutcode voor bestaand object | `ORA-00955` | `psycopg2.errors.DuplicateTable` |
| CLOB type | `CLOB` | `TEXT` |
| LLM client | `OpenAI()` met `gpt-5` | `anthropic.Anthropic()` met `claude-sonnet-4-6` |

**Alles wat niet in de bovenste rij staat is direct herbruikbaar:** de MemoryManager logica, de summarisatieflows, de entity extractie, de tool offloading structuur, de JIT expansion. Dat is 90% van de waardevolle code.

---

## 7. Wat direct copy-paste bruikbaar is (na kleine aanpassingen)

### Direct bruikbaar (alleen connectie/syntax swap)

1. **`MemoryManager` klasse-structuur** -- vervang Oracle cursor syntax door psycopg2 `%s` placeholders en `cursor.fetchone()` voor RETURNING
2. **`write_tool_log` / `read_tool_log`** -- identieke logica, alleen SQL syntax
3. **`summarise_context_window`** -- vervang OpenAI client door Anthropic SDK
4. **`offload_to_summary`** -- volledig database-agnostisch, direct bruikbaar
5. **`mark_as_summarized` / `get_unsummarized_messages`** -- alleen SQL dialect aanpassen
6. **`read_summary_context`** -- volledig bruikbaar als context-pointer patroon
7. **`calculate_context_usage`** -- volledig database-agnostisch
8. **Entity extraction prompt** -- identiek herbruikbaar, model wisselen

### Aanpassen maar weinig werk

9. **`embed_and_store`** -- HuggingFaceEmbeddings wrapper vervangen door directe `sentence-transformers` aanroep
10. **`vector_search`** -- `OracleVS.similarity_search()` vervangen door pgvector `<=>` operator query
11. **Tabelschema's** -- Oracle DDL naar PostgreSQL DDL (CLOB -> TEXT, SYS_GUID() -> gen_random_uuid(), etc.)

### Niet bruikbaar (Oracle-specifiek)

- `setup_oracle_database()` -- complete Oracle Docker setup
- `connect_to_oracle()` -- oracledb specifiek
- `safe_create_index()` met ORA-00955 check
- `langchain_oracledb` imports

---

## 8. Zes geheugentypen -- overzicht en relevantie myPKA

| Geheugentype | Tabel | Doel | Relevant voor myPKA |
|---|---|---|---|
| Conversational | SQL tabel | Recente ongesummariseerde berichten | Sessiecontext per agent |
| Knowledge Base | Vector store | Documenten, facts, zoekresultaten | Kennisbank per domein |
| Workflow | Vector store | Succesvolle tool-sequences hergebruiken | Agent taakpatronen |
| Toolbox | Vector store | Tool definities semantisch opvraagbaar | Dynamisch tool routing |
| Entity | Vector store | Personen, projecten, systemen | CRM-extractie, Penn journaling |
| Summary | Vector store + SQL | Gecomprimeerde oude context (JIT expansie) | Lange sessies borgen |
| Tool Log | SQL tabel | Volledige tool outputs offloaden | Grote outputs buiten context |

---

## Aanbeveling richting Kai

Dit notebook levert de volledige blauwdruk voor de myPKA Unified Memory Core. De architecturale keuzes (aparte geheugentypen, JIT expansion, tool offloading) zijn solide en direct toepasbaar. Kai hoeft geen nieuwe architectuur te ontwerpen -- het vertaalwerk van Oracle naar PostgreSQL is mechanisch. Ik adviseer Kai om:

1. De `MemoryManager` klasse als startpunt te nemen en de Oracle-specifieke delen te vervangen
2. Een enkele `memory_vectors` tabel te gebruiken met een `memory_type` kolom in plaats van losse tabellen per type (eenvoudiger beheer)
3. De tool offloading als eerste te implementeren -- meest directe waarde voor context management
4. Entity extraction te activeren voor Penn's journaalverwerking

---

*This belongs in:* **Team Knowledge/Core** (technische infrastructuur) en **P-Unified Memory Core** (project deliverable).

---
Delivered on: 2026-05-20
Delivered at: P-Unified Memory Core
