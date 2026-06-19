# Session Log — Sasha Shopify Setup + AI Cost Reduction Research

**Date:** 2026-05-02
**Database:** team-knowledge.db — session id: 14
**Topics:** shopify-setup, team-management, cost-reduction, infrastructure

## Summary

This session established Sasha's official Shopify connection using the Shopify AI Toolkit plugin (v1.2.1) and Shopify CLI with full Admin API scopes against ynmuzt-xm.myshopify.com. Sasha's CLAUDE.md was updated with the correct toolset, he/him pronouns, English-only content, and a mandatory pre-change summary protocol (Entity, Command, Before, After) before any mutation. Pax researched Ollama and OpenRouter as token cost reduction strategies; findings showed OpenRouter free tier is blocked by rate limits and lack of tool use, making it unsuitable for Pax agentic sessions. Ollama was installed via winget but the qwen3.5:9b model pull is still pending. A comprehensive disaster recovery SOP was created and registered in the SOP index.

## Decisions

- Sasha uses official Shopify AI Toolkit plugin + CLI (not community shopify-mcp)
- Pre-change summary required before any Shopify mutation (Entity, Command, Before, After)
- Sasha is male (he/him); team gender balance to be maintained role-appropriately
- OpenRouter free tier not suitable for Pax agentic sessions (tool-use blocker)
- Ollama is the preferred path for free local model inference for Pax

## Actions Taken

- Enabled shopify-plugin@shopify-ai-toolkit v1.2.1
- Authenticated Shopify CLI against ynmuzt-xm.myshopify.com with full Admin API scopes
- Updated Sasha CLAUDE.md: toolset, pronouns, EN language, approval rule
- Fixed page typo "Shippping and Delivery" → "Shipping and Delivery"
- Created and deleted test page to verify full CRUD access
- Created SOP-001_Disaster recovery.md SOP and registered in SOP-index.md
- Installed Ollama via winget

## Delegations

- Sasha: fix page title typo (success)
- Sasha: create + delete test page (success)
- Pax: research Ollama/OpenRouter token reduction strategies (success)

## Open Items

- Pull qwen3.5:9b model in external terminal (owner action)
- Finalize Pax + Ollama integration architecture
