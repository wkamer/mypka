# Shopify connection audit and full reset

**Date:** 2026-05-02
**Domain:** Kamer E-commerce
**DB row id:** 4
**Topics:** shopify, sasha, mcp, integration

## Summary

Session focused on auditing and resetting Sasha's Shopify toolset. The AI Toolkit plugin and an existing .mcp.json MCP server were both active but overlapping; the MCP server lacked pages support and pointed to an unrecognized store domain. After investigating options for adding full Admin API access including pages, the owner chose to wipe all three integration points and start fresh. Sasha's CLAUDE.md was reset to reflect no active Shopify connection.

## Decisions

- Remove all existing Shopify integrations (plugin + MCP server + marketplace entry) and start fresh
- New connection must use a proper Admin API token with full scopes including pages

## Actions Taken

- Verified plugin operational for products/orders/customers via Sasha delegation
- Discovered pages not supported by existing tools
- Found .mcp.json with old OAuth credentials for unrecognized domain (ynmuzt-xm.myshopify.com)
- Removed shopify entry from .mcp.json
- Removed shopify-plugin@shopify-ai-toolkit from .claude/settings.json
- Removed shopify-ai-toolkit from ~/.claude/settings.json extraKnownMarketplaces
- Reset Sasha's CLAUDE.md toolset section to no active connection

## Delegations

- Sasha — plugin verification (products, orders, customers)

## Open Items

- Set up fresh Shopify connection with Admin API token covering full scopes (products, orders, customers, pages, themes)
