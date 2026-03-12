---
name: bitrix-grid-migration
description: Migrate or estimate migration from DataTables (or custom JS tables) to Bitrix Grid (`bitrix:main.ui.grid`). Use when replacing table UI/UX, planning phased migration, or estimating effort for Bitrix Grid adoption.
---

# Bitrix Grid Migration

## Decision gate (ask before acting)

- Target UI scope (specific screens or full replacement).
- Must-keep behaviors (custom sort, responsive, fixed headers/columns).
- Data volume and performance constraints.

## Workflow

1. Inventory DataTables usage.
   - Find `new DataTable`, `.DataTable()`, `.dataTable()` occurrences.
   - List component paths and templates.
2. Classify table complexity.
   - Simple: sorting, paging, basic filters.
   - Medium: fixed header/columns, responsive, custom renderers.
   - Heavy: grouped columns, custom ordering, multi-view (desktop/mobile).
3. Define target Grid pattern.
   - Standardize: Grid + Filter + AJAX.
   - Define backend pagination and sorting.
4. Estimate and phase.
   - Pilot on a medium screen.
   - Sequence by risk and dependency.

## Output checklist

- Affected files list with paths.
- Feature parity matrix (DataTables -> Grid).
- Risks and regressions (mobile/responsive, custom sort).
- Phased plan and time estimates.

## When to load references in this skill

- Use `references/dt-to-grid.md` for a concrete estimate template and known risks.
