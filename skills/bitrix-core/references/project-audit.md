# Bitrix Project Audit Checklist

Use this checklist to quickly audit Bitrix/Bitrix24 projects. Keep outputs factual and actionable.

## Core completeness

- Check `bitrix/modules` exists.
- Check `bitrix/templates` or `local/templates`.
- Check `upload/` and size considerations.
- Check `local/` and `local/modules`.

## Environment

- PHP version and target minimum.
- Web server and PHP-FPM/Apache mode.
- DB engine and version.
- Cache and session storage settings.

## Code and structure

- Components: `local/components/*`.
- Modules: `local/modules/*`, `bitrix/modules/*`.
- Agents: `bitrix/php_interface/init.php` and agents registration.
- Migrations: `bitrix/modules/sprint.migration` or other tools.

## Dependency risk

- `composer.json` in `local/` or modules.
- Find heavy parsers: PDF, spreadsheet, HTML rendering.
- Identify unused packages and plugins.

## Performance and ops risk

- Large DB tables (sessions, order change logs).
- Long-running agents or imports.
- External integrations (1C exchange, CRM, telephony).

## Output template

1. Summary: 2-4 bullets.
2. Findings: list with paths and evidence.
3. Risks: list of top 3-5.
4. Next steps: concrete actions with commands.
