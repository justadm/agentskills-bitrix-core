# Agent Skills for Bitrix/Bitrix24

## How to use

1. Install skills in your Codex environment and make sure `skills/` is accessible.  
2. Build the knowledge base using the wiki pipeline:
   - Scrape sources:
     - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_scrape.py --config /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_config.json --out /Users/just/projects/AgentSkills/Bitrix/wiki --cache /Users/just/projects/AgentSkills/Bitrix/wiki/sources/_cache`
   - Build indexes:
     - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_build.py --root /Users/just/projects/AgentSkills/Bitrix/wiki --methods-compact`
   - Validate:
     - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_validate.py --index /Users/just/projects/AgentSkills/Bitrix/wiki/api/index.json`
3. Methods-only search:
   - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_search.py --root /Users/just/projects/AgentSkills/Bitrix/wiki --q "user\\.get" --methods-only`
4. Use skills for tasks:
   - `bitrix-core` for audits, migrations, architecture, and support.
   - `bitrix-grid-migration` for DataTables to Bitrix Grid migration.
   - `bitrix24-marketplace` for Marketplace readiness.
   - `bitrix-ops-incident` for incident response and hotfixes.

## Real benefits

- Fast access to structured REST method data without manual doc browsing.
- Consistent schema for params, errors, and examples for automation and integrations.
- Skills encode repeatable workflows and reduce missed steps.
- Local cache and incremental updates speed up rebuilds.

## Distribution

1. GitHub repository:
   - Publish `skills/` and `wiki/` in a dedicated repo.
   - Add a short README with install and build commands.
2. Internal registry:
   - Keep skills in a private repo and attach via submodule or internal package manager.
3. Build artifacts:
   - Publish `wiki/api/*.json` and `wiki/wiki/*.md` as release artifacts.
4. CI/CD:
   - Run nightly builds and publish `wiki/` via GitHub Pages or artifacts.
   - Gate releases on `bitrix_wiki_validate.py`.

## Recommended update order

1. Refresh sources.
2. Rebuild indexes.
3. Validate.
