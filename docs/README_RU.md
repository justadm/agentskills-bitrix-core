# Agent Skills для Bitrix/Bitrix24

## Как пользоваться

1. Установи skills в своем окружении Codex и убедись, что папка `skills/` доступна.  
2. Для работы с базой знаний используй генератор wiki и индексы:
   - Сбор источников:
     - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_scrape.py --config /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_config.json --out /Users/just/projects/AgentSkills/Bitrix/wiki --cache /Users/just/projects/AgentSkills/Bitrix/wiki/sources/_cache`
   - Построение индексов:
     - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_build.py --root /Users/just/projects/AgentSkills/Bitrix/wiki --methods-compact`
   - Проверка корректности индекса:
     - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_validate.py --index /Users/just/projects/AgentSkills/Bitrix/wiki/api/index.json`
3. Быстрый поиск по методам:
   - `python3 /Users/just/projects/AgentSkills/Bitrix/scripts/bitrix_wiki_search.py --root /Users/just/projects/AgentSkills/Bitrix/wiki --q "user\\.get" --methods-only`
4. При решении задач используйте skills:
   - `bitrix-core` для аудита, миграций, архитектуры и поддержки.
   - `bitrix-grid-migration` для перехода на Bitrix Grid.
   - `bitrix24-marketplace` для подготовки к Marketplace.
   - `bitrix-ops-incident` для инцидентов и аккуратных хотфиксов.

## Реальные плюсы

- Быстрый доступ к структурированным данным по методам REST, без ручного поиска в документации.
- Единый формат для параметров, ошибок и примеров; проще писать интеграции и автоматизацию.
- Повторяемые процедуры в навыках уменьшают риск регрессий и потери важного шага.
- Локальный кеш и инкрементальные обновления уменьшают время прогонов.

## Как распространять

1. GitHub репозиторий:
   - Публикуй `skills/` и `wiki/` в отдельном репозитории.
   - Добавь краткую README с установкой и командами сборки.
2. Внутренний регистр навыков:
   - Храни навыки в приватном репозитории и подключай в CI/CLI в качестве submodule или через внутренний пакетный менеджер.
3. Артефакты сборки:
   - Для внешних пользователей можно публиковать только `wiki/api/*.json` и `wiki/wiki/*.md` как артефакт релиза.
4. CI/CD:
   - Запусти сборку wiki по расписанию (например, nightly) и публикуй `wiki/` как артефакт или GitHub Pages.
   - В пайплайне запускай `bitrix_wiki_validate.py` и блокируй релиз при ошибках.

## Рекомендуемый порядок обновления

1. Обновить wiki источники.
2. Пересобрать индексы.
3. Прогнать валидацию.
