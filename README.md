# ДЗ-1 «Среда и контекст»: исследование TiN

Небольшая исследовательская задача: извлечь условия лазерного синтеза TiN
из статьи, проверить утверждения по первоисточнику, построить память и граф
проекта, сравнить поиск и собрать связанную литературу.

**Источник:** Popov et al., *Laser-ablative synthesis of plasmonic TiN nanoparticles
for biomedical applications*, Scientific Reports 9, 1194 (2019).
[DOI: 10.1038/s41598-018-37519-1](https://doi.org/10.1038/s41598-018-37519-1).

## Результаты

| Блок | Артефакты |
|---|---|
| Условия и результаты опытов: 27 записей с цитатами и страницами | [conditions.csv](results/conditions.csv), [conflicts.md](results/conflicts.md) |
| Сжатие в отдельных контекстах L1 → L2 → L3 | [memory/](memory/), [проверка тезисов](evidence/thesis_verification.json) |
| Онтология: 8 классов, 4 правила, 25 объектов; две сессии графа | [ontology.yaml](ontology.yaml), [graph_view.md](graph_view.md), [graph_literature.md](graph_literature.md) |
| Выполненные ноутбуки недель 3 и 5 | [agent_loop_TiN.ipynb](notebooks/agent_loop_TiN.ipynb), [search_lab_TiN.ipynb](notebooks/search_lab_TiN.ipynb) |
| BM25 и dense: 20 аннотаций, 5 запросов, 5 комментариев | [my_search_report.md](reports/my_search_report.md) |
| Пять обзоров, OpenAlex, Wikidata/SPARQL, проверка метаданных | [literature_mcp.md](reports/literature_mcp.md) |
| Сравнение с/без AGENTS и проверка ограничений агента | [agents_comparison.md](reports/agents_comparison.md), [diary.md](diary.md), [evidence/](evidence/) |

Карта файлов — [INDEX.md](INDEX.md).

## Проверка

Python 3.12. Из корня репозитория:

```console
python -m pip install -r requirements.txt
python checks/check.py all
python checks/replay_search.py
python checks/submission_ready.py
```

Проверки не требуют ключей, сети или скачивания модели. Проверяются структура,
цитаты, контрольные числа, граф, пересчёт сохранённого поиска и запись приёмки.
Последние результаты — [evidence/final_verification.json](evidence/final_verification.json).
На Windows те же команды запускает `CHECK.cmd`.

## Среда и авторство

Основные прогоны: **OpenCode 2.0.16 / DeepSeek V4.1 Flash Free**.
Независимые проверки и интеграция подготовлены с помощью отдельного ИИ.
Дополнительно использованы **AI4Science / Goose 1.50.0 / Yandex DeepSeek V4 Flash**.
В ноутбуке число повторений уменьшено с 12/8 до 3; qwen235 был недоступен
(PermissionDeniedError), GPT-OSS120B и DeepSeek работали. Основная серия
OpenCode и отдельные прогоны AI4Science сохранены раздельно.

`[порождено]` — текст ИИ; `[источник]` — исходные данные;
`[написано]` — комментарии, подтверждённые студентом.
Пять комментариев находятся в отчёте поиска; запись проверок и приёмки —
в `student_review.json`. Автоматическая проверка и подтверждение студента разделены.
Реальные ошибки и превышения бюджета сохранены в журналах.

## Воспроизводимость и источники

Метаданные, ответы API и векторы сохранены. Для повторного запуска ноутбуков
используются `requirements-notebooks.txt` и локальные переменные по `.env.example`.
Секретные ключи и установленные окружения в репозиторий не входят.

PDF включён по **CC BY 4.0**, без изменения оригинала.
Авторы, лицензия и контрольные суммы — [paper/source.json](paper/source.json).
Заимствованные материалы — [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
