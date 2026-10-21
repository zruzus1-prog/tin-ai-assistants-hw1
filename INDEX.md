# Указатель проекта TiN

[порождено] Быстрый вход: сначала читать этот файл и `STATUS.md`.

| Путь | Зачем открывать |
|---|---|
| `README.md` | Результаты и команды проверки |
| `STATUS.md` | Готовность и оставшиеся действия |
| `AGENTS.md` | Цель, ограничения, бюджет и договор с агентом |
| `paper/article.pdf` | Первоисточник Popov et al., 11 страниц, CC BY 4.0 |
| `paper/source.json`, `paper/pages/` | Метаданные, хеши и текст с номерами страниц |
| `results/conditions.csv` | 27 извлечённых условий и результатов с цитатами |
| `results/conflicts.md` | Расхождение μJ/mJ и другие ограничения |
| `memory/L1.md`, `memory/cascade/` | Сжатия трёх частей в отдельных окнах |
| `memory/L2.md`, `memory/theses.json` | Девять проверяемых тезисов и записи сверки |
| `memory/L3.md` | Итог одной строкой |
| `ontology.yaml`, `ontology/` | Восемь классов, типы отношений и четыре правила |
| `notes/`, `tasks/` | Объекты графа, задачи и результаты двух сеансов |
| `graph_view.md`, `graph_literature.md` | Два представления графа в Mermaid |
| `library/corpus.jsonl` | 20 работ с аннотациями для своего поиска |
| `library/rankings.json`, `*_vectors.npy`, `encoder.json` | Замороженные ранжирования, реальные векторы и версия кодировщика |
| `library/reviews.json`, `query_notes.json`, `targeted_queries.json` | Пять обзоров и происхождение поиска |
| `notebooks/search_lab_TiN.ipynb` | Выполненный ноутбук недели 5 |
| `notebooks/agent_loop_TiN.ipynb`, `journal.csv` | Реальный цикл агента недели 3, собственная задача и φ |
| `reports/my_search_report.md` | Пять сравнений BM25/dense и пять комментариев `[написано]` |
| `reports/literature_mcp.md` | Итог поиска и независимой сверки издателей |
| `checks/check.py` | Формат, цитаты, контрольные числа, правила графа, состав поиска |
| `checks/replay_search.py` | Пересчёт BM25 и cosine-ранжирований **без сети и LLM** |
| `checks/submission_ready.py` | Отдельная проверка реальных собственных комментариев/приёмки |
| `src/research_mcp.py` | Неизменённый модуль MCP из материалов курса |
| `src/run_research_mcp.py` | Запуск модуля с ключом из окружения и аудитом GET-запросов |
| `evidence/runs/`, `evidence/run_summary.json` | Реальные журналы DeepSeek/OpenCode, а не пересказ действий |
| `evidence/context_ablation/` | Два действительных прогона со строкой соглашения и без неё |
| `evidence/ai4science_*` | Установка, doctor и действительный запуск Goose/Yandex |
| `evidence/research_api_calls.jsonl` | Ответы OpenAlex/Wikidata с редактированными параметрами запроса |
| `evidence/publisher_verification.json`, `thesis_verification.json` | Что проверил ИИ; студентская проверка выделена отдельно |
| `evidence/checker_negative_cases.json` | Шесть испорченных примеров, которые валидатор отверг |
| `diary.md` | Журнал реальных действий, сбоев, исправлений и кодов проверки |

Ключи и установленные окружения не входят в репозиторий.
Локальный `.env` и `opencode.jsonc` не публикуются.
