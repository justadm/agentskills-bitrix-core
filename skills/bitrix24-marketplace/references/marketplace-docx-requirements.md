# Marketplace Docx Requirements (Condensed)

Source: `/Users/just/Sites/ofs/b24.loc/.docs/b24_market/2026-02-25_marketplace_docx_requirements_action_plan.md`

## Required files

- `install/index.php`
- `install/version.php`
- `include.php`

## Common rejection causes

- Missing or invalid version.
- Missing `MODULE_ID`, `PARTNER_NAME`, `PARTNER_URI`.
- Incorrect module class name.

## Packaging notes

- First upload is full build archive.
- Updates are versioned archives (alpha/beta/stable).
- On macOS for tar: `export COPYFILE_DISABLE=true`.
