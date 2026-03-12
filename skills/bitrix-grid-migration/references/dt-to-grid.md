# DataTables to Bitrix Grid Notes

Source evidence: `/Users/just/Sites/lk.loc/docs/estimate-datatables-to-bitrix-grid-2026-03-05.md`

## Typical findings

- DataTables often loaded globally in template header.
- Multiple components use DataTables API.
- Heavy tables can rely on fixed columns/headers, responsive, custom ordering.

## Estimation pattern

1. Inventory + architecture: 5-8 days.
2. Grid adapter (sorting/paging/filter): 6-10 days.
3. Simple screens: 12-20 days.
4. Heavy screens: 8-16 days per group.
5. Mobile scenarios: 6-10 days.
6. Regression and UX polish: 10-15 days.

## Risks

- Loss of current behavior (custom ordering, column groups).
- Mobile regressions (DataTables Responsive).
- Backend pagination and data fetch performance.

## Phasing

- Pilot one medium screen.
- Roll out in waves by domain area.
- Remove global DataTables only after full cutover.
