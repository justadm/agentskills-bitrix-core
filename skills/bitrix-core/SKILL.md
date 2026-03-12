---
name: bitrix-core
description: Bitrix/Bitrix24 project setup, architecture, audits, migrations, and support. Use when Codex needs to create, refactor, estimate, or troubleshoot Bitrix/Bitrix24 projects (core, modules, components, templates, local/php_interface, migrations, performance, or environment checks).
---

# Bitrix Core

## Quick start

1. Identify project type and scope.
   - Bitrix vs Bitrix24, on-prem vs cloud, versions, web server, PHP, DB.
   - Check project roots: `bitrix/`, `local/`, `upload/`, `vendor/`, `www/`.
2. Collect evidence from repo or docs.
   - Scan project docs and audits when present.
   - Prefer factual lists: affected components, files, and steps.
3. Use Bitrix REST docs via MCP tools when needed.
   - Use `mcp__bx24-mcp__bitrix-search` then `mcp__bx24-mcp__bitrix-method-details`.
   - MCP server reference: https://mcp-dev.bitrix24.tech/mcp

## Standard workflow

## Decision gate (ask before acting)

- Project type (Bitrix vs Bitrix24, box vs cloud), target version, and environment.
- Primary goal (audit, migration, feature build, incident).
- Access scope (repo, server, DB, logs).

1. Baseline checks.
   - Confirm `bitrix/modules` exists (core completeness).
   - Confirm templates in `bitrix/templates` or `local/templates`.
   - Confirm `upload/` presence and cache directories to ignore.
2. Architecture map.
   - Identify main components in `local/components`.
   - Identify `local/modules` and `bitrix/modules` usage.
3. Risk and dependency scan.
   - Look for `composer.json` in `local/` and module roots.
   - Identify unused libraries and security-sensitive parsers.
4. Output format.
   - Provide a short summary, concrete findings, and next steps.
   - Include exact paths and commands.

## Local references to consult when relevant

- Migration estimates and risk notes:
  - `/Users/just/Sites/lk.loc/docs/estimate-bitrix-migration-1ckab-2026-03-05.md`
  - `/Users/just/Sites/lk.loc/docs/estimate-datatables-to-bitrix-grid-2026-03-05.md`
  - `/Users/just/Sites/lk.loc/docs/task-19800-library-risk.md`
- JS/module audit examples:
  - `/Users/just/Sites/lk.loc/docs/js-modules-audit-2026-03-05.md`

## When to load references in this skill

- Use `references/project-audit.md` for a reusable audit checklist.

## Wiki/API integration

- If the local wiki exists, prefer it before live web fetching.
- Wiki root: `/Users/just/projects/AgentSkills/Bitrix/wiki`.
- API index: `/Users/just/projects/AgentSkills/Bitrix/wiki/api/index.json`.
