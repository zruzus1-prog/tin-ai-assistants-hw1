---
type: ЗапросКГрафу
date: 2026-10-20
---

# Query-OpenAlex-PLAL

- тип: [[ЗапросКГрафу]]

## Происхождение

- **Источник:** OpenAlex API через research MCP: `openalex_search`, `openalex_links`, `openalex_work`.
- **Дата:** 2026-10-20.
- **Статус:** выполнен.
- **Сохранённый ответ:** [library/query_notes.json](../library/query_notes.json).

## Основной запрос

- **Точный запрос:** `laser ablation in liquids nanoparticles`
- **Параметры:** `work_type=review`, `year_from=2016`, `year_to=2026`, `sort=cited_by_count`, `limit=10`.
- **Полученные IDs:** `W2587989553`, `W4367393972`, `W4388628377`, `W4404121073`, `W2969326827`.

## Дополнительные запросы

| Точный запрос | Параметры | Найдено |
|---|---|---|
| `pulsed laser ablation in liquid nanoparticle synthesis` | `work_type=review`, `year_from=2016`, `year_to=2026`, `sort=relevance`, `limit=20` | 450 |
| `laser fragmentation nanoparticles in liquid` | `work_type=review`, `year_from=2016`, `year_to=2026`, `sort=relevance`, `limit=10` | 218 |
| `laser-generated colloidal nanoparticles` | `work_type=review`, `year_from=2016`, `year_to=2026`, `sort=relevance`, `limit=10` | 674 |

## Примечание

Запросы и параметры приведены по сохранённому JSON; результаты не пересчитывались в этой сессии.

[порождено]
