---
name: bitrix24-marketplace
description: Prepare Bitrix/Bitrix24 modules for Marketplace submission and updates. Use when packaging modules, running prechecks, validating install/update/rollback flows, or assembling marketplace card materials (description, screenshots, legal docs).
---

# Bitrix24 Marketplace

## Decision gate (ask before acting)

- Module ID and code ownership.
- Current version and release type (alpha/beta/stable).
- Target portal type (cloud vs box) and PHP versions.

## Workflow

1. Validate module structure.
   - `install/index.php`, `install/version.php`, `include.php`.
   - Correct module ID and class name.
2. Run precheck and smoke tests.
   - Use project precheck scripts when available.
   - Validate install/update/uninstall and rollback path.
3. Review quality and security checklist.
   - No warnings, no JS errors, no unsafe logging.
   - Proper permissions and REST rate handling.
4. Assemble marketplace card.
   - Description, limits, screenshots, changelog, legal pages.

## Output checklist

- Precheck results.
- Install/update/uninstall/rollback status.
- PHP version coverage.
- Card readiness items (text, images, legal).

## When to load references in this skill

- Use `references/marketplace-checklist.md` for full submission checklist.
- Use `references/marketplace-docx-requirements.md` for docx-specific requirements.
- Use `references/php-versions.md` for PHP runtime matrix and lint commands.
