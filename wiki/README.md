# Bitrix Knowledge Base

This folder contains a generated Wiki and a JSON API index derived from Bitrix/Bitrix24
documentation and internal references. It is designed to be read by skills and tools.

## Layout

- `sources/` raw pages and metadata
- `wiki/` normalized Markdown pages
- `api/` JSON index for programmatic lookup

## Regeneration

Use scripts in `scripts/` to crawl/parse sources and rebuild the wiki and API.

## Suggested flow

1. Clone required sources locally.
2. Run `bitrix_wiki_scrape.py` with `--config` to ingest sources.
3. Run `bitrix_wiki_build.py` to regenerate the wiki index.

## Example commands

```bash
# Clone dev hub (once)
git clone https://github.com/bitrix-tools/bitrix24-dev-hub \
  /Users/just/projects/AgentSkills/Bitrix/wiki/sources/repos/bitrix24-dev-hub

# Fetch and ingest
python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_scrape.py \
  --config /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_config.json \
  --out /Users/just/projects/AgentSkills/Bitrix/wiki \
  --cache /Users/just/projects/AgentSkills/Bitrix/wiki/sources/_cache

# Build index
python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_build.py \
  --root /Users/just/projects/AgentSkills/Bitrix/wiki

# Search
python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_search.py \
  --root /Users/just/projects/AgentSkills/Bitrix/wiki --q "crm"

# Methods-only search
python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_search.py \
  --root /Users/just/projects/AgentSkills/Bitrix/wiki --q "user\\.get" --methods-only

# Validate index
python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_validate.py \
  --index /Users/just/projects/AgentSkills/Bitrix/wiki/api/index.json
```

## Section indexes

- `api/index_by_section.json` groups entities by top-level section (first tag).
- `api/methods.json` contains only API methods.
- `api/index_compact.json` is a lightweight list for quick lookup.
