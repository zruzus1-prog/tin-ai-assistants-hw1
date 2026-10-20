---
type: ЗапросКГрафу
date: 2026-10-20
---

# Query-Targeted-2

- тип: [[ЗапросКГрафу]]

## Происхождение

- **Источник:** OpenAlex, targeted exact-title search (`work_type=any`).
- **Дата:** 2026-10-20.
- **Сохранённый ответ:** [library/targeted_queries.json](../library/targeted_queries.json).
- **Publisher reference:** Kim M., Osone S., Kim T., Higashi H., Seto T. (2017). Synthesis of nanoparticles by laser ablation: a review. KONA Powder and Particle Journal 34:80–90.

## Запрос

- **Точный запрос:** `Synthesis of nanoparticles by laser ablation: a review`
- **Параметры:** `work_type=any`, `year_from=2016`, `year_to=2026`, `sort=relevance`, `limit=3`.
- **Найдено:** 81250.
- **Полученные IDs:** `W2344885033`, `W4318820635`, `W4283316521`.
- **Выбранный ID:** `W2344885033`.
- **Совпадение:** `exact_title`.

## Примечание

Фильтр типа намеренно не применялся. Для выбранного совпадения отдельно вызван `openalex_work`; фактический тип графа сохранён без изменения.

[порождено]
