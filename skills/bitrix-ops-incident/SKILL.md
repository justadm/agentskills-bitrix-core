---
name: bitrix-ops-incident
description: Bitrix operational support and incident response. Use when diagnosing production issues (timeouts, 1C exchange, cache, missing core), preparing or applying hotfixes, or deploying via FTP scripts.
---

# Bitrix Ops and Incident Response

## Decision gate (ask before acting)

- Scope (prod/stage/local) and impact.
- Access to logs/SSH/FTP.
- Allowed changes window and rollback constraints.

## Workflow

1. Triage scope and impact.
   - Identify error page, status codes, and affected routes.
2. Check core completeness and config.
   - Verify `bitrix/modules`, templates, `upload/`.
   - Review `.settings.php` and logging/debug flags.
3. Inspect logs and timeouts.
   - Web server logs, PHP errors, Bitrix logs.
4. Apply minimal hotfixes.
   - Guard undefined constants, fix broken markup, clear cache.
5. Deploy safely.
   - Use dry-run in FTP deploy scripts before `--apply`.

## When to load references in this skill

- Use `references/korzina-incident.md` for a real-world incident checklist.
- Use `references/ftp-deploy.md` for FTP deploy procedure.
