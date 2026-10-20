---
type: ЗапросКГрафу
date: 2026-10-20
---

# Query-Wikidata-TiN

- тип: [[ЗапросКГрафу]]

## Происхождение

- **Источник:** Wikidata API и Wikidata Query Service через research MCP: `wikidata_search`, `wikidata_sparql`.
- **Дата:** 2026-10-20.
- **Статус:** выполнен.
- **Сохранённый ответ:** [library/query_notes.json](../library/query_notes.json).

## Поиск сущности

- **Точный запрос:** `titanium nitride`
- **Параметры:** `language=en`, `limit=5`.
- **Полученные IDs:** `Q415638`.

## SPARQL

```sparql
SELECT ?label ?instanceOf ?instanceOfLabel ?formula WHERE { OPTIONAL { wd:Q415638 rdfs:label ?label . FILTER(LANG(?label) = "en") } OPTIONAL { wd:Q415638 wdt:P31 ?instanceOf . } OPTIONAL { wd:Q415638 wdt:P274 ?formula . } SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } } LIMIT 10
```

## Зафиксированные сведения

- Сущность: `Q415638` (titanium nitride).
- Свойство `P31` (instance of) входило в запрос; отдельное значение в сохранённом срезе `query_notes.json` не зафиксировано.
- Свойство `P274` (chemical formula): `NTi`.

## Оговорка

Строка `NTi` приведена как внешний ответ Wikidata. Порядок элементов не исправлялся вручную и не является утверждением о предпочтительной записи формулы TiN.

[порождено]
