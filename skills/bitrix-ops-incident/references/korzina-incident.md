# Incident Notes: korzina.su (Condensed)

Source: `/Users/just/Sites/XA/korzina.su/docs/2026-03-11_audit.md`

## Typical issues

- Incomplete Bitrix core (missing `bitrix/modules`).
- Missing templates (`bitrix/templates` or `local/templates`).
- Debug enabled in production.
- Undefined constants in templates under PHP 8.3.
- 1C exchange timeouts and large DB tables.

## Safe hotfix patterns

- Guard constants with `defined()` before use.
- Remove broken markup sections instead of patching CSS.
- Clear Bitrix cache directories after fix.

## Ops checks

- Verify SSH/FTP reachability and credentials.
- Check web server timeouts and PHP limits.
- Monitor Apache/Nginx logs during exchange.

## Database hygiene

- Watch `b_user_session`, `b_sale_order_change`, archives.
- Consider cleanup and `OPTIMIZE` after confirmation.
