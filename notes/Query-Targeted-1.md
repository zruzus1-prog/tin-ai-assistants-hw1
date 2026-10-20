---
type: ЗапросКГрафу
date: 2026-10-20
---

# Query-Targeted-1

- тип: [[ЗапросКГрафу]]

## Происхождение

- **Источник:** OpenAlex, targeted exact-title search (`work_type=any`).
- **Дата:** 2026-10-20.
- **Сохранённый ответ:** [library/targeted_queries.json](../library/targeted_queries.json).
- **Publisher reference:** Xiao J., Liu P., Wang C.X., Yang G.W. (2017). External field-assisted laser ablation in liquid: an efficient strategy for nanocrystal synthesis and nanostructure assembly. Progress in Materials Science 87:140–220.

## Запрос

- **Точный запрос:** `External field-assisted laser ablation in liquid: an efficient strategy for nanocrystal synthesis and nanostructure assembly`
- **Параметры:** `work_type=any`, `year_from=2016`, `year_to=2026`, `sort=relevance`, `limit=3`.
- **Найдено:** 3650.
- **Полученные IDs:** `W2590450430`, `W4283316521`, `W2802854090`.
- **Выбранный ID:** `W2590450430`.
- **Совпадение:** `exact_title`.

## Примечание

Фильтр типа намеренно не применялся. Для выбранного совпадения отдельно вызван `openalex_work`; фактический тип графа сохранён без изменения.

[порождено]
