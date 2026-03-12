# FTP Deploy Procedure (Condensed)

Source: `/Users/just/Sites/XA/watchcases/docs/deploy.md`

## Requirements

- `lftp` installed.
- `.env` contains FTP and Prod sections.

## Commands

- Dry-run: `./deploy_ftp.sh`
- Apply: `./deploy_ftp.sh --apply`
- Range: `./deploy_ftp.sh --base <ref> --apply`
- Full: `./deploy_ftp.sh --all --apply`

## Notes

- Script creates remote backup by default.
- Use `--no-backup` only when explicitly allowed.
