# Agent Skills for Bitrix/Bitrix24

Этот репозиторий содержит набор Agent Skills и локальную базу знаний по Bitrix/Bitrix24.

## Состав

- `skills/` — навыки для Codex (аудит, миграции, marketplace, инциденты).
- `wiki/` — локальная wiki и JSON‑API индексы.
- `scripts/` — сборка, поиск, валидация.
- `docs/` — документация (RU/EN).

## Быстрый старт

Сбор и индексация:

```
python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_scrape.py \
  --config /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_config.json \
  --out /Users/just/projects/AgentSkills/Bitrix/wiki \
  --cache /Users/just/projects/AgentSkills/Bitrix/wiki/sources/_cache

python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_build.py \
  --root /Users/just/projects/AgentSkills/Bitrix/wiki --methods-compact
```

Документация:

- `/Users/just/projects/AgentSkills/Bitrix/docs/README_RU.md`
- `/Users/just/projects/AgentSkills/Bitrix/docs/README_EN.md`
