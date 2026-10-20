# Граф литературы: сессия 2

[порождено] Продолжение графа проекта; старый `graph_view.md` не изменялся. Схема отражает только новые заметки этой сессии и разрешённые связи онтологии.

```mermaid
flowchart LR
    subgraph Sources["Источники"]
        S1["Review-W2587989553<br/>Zhang et al., 2017<br/>Chemical Reviews"]
        S2["Review-W2344885033<br/>Kim et al., 2016<br/>KONA"]
        S3["Review-W2590450430<br/>Xiao et al., 2017<br/>Prog. Mater. Sci."]
        S4["Review-W4367393972<br/>Attallah et al., 2023<br/>Plasmonics"]
        S5["Review-W4388628377<br/>Alheshibri, 2023<br/>Nanomaterials"]
    end

    subgraph Queries["Запросы к графу"]
        Q1["Query-OpenAlex-PLAL"]
        Q2["Query-Targeted-1"]
        Q3["Query-Targeted-2"]
        Q4["Query-Wikidata-TiN"]
    end

    M["Literature-Extraction"]
    T["Task-Literature-Session-2"]

    S1 -->|найденЗапросом| Q1
    S4 -->|найденЗапросом| Q1
    S5 -->|найденЗапросом| Q1
    S3 -->|найденЗапросом| Q2
    S2 -->|найденЗапросом| Q3

    S1 -->|связанСМетодом| M
    S2 -->|связанСМетодом| M
    S3 -->|связанСМетодом| M
    S4 -->|связанСМетодом| M
    S5 -->|связанСМетодом| M

    T -->|основанаНа| M
    T -->|создаёт| S1
    T -->|создаёт| S2
    T -->|создаёт| S3
    T -->|создаёт| S4
    T -->|создаёт| S5
    T -->|создаёт| Q1
    T -->|создаёт| Q2
    T -->|создаёт| Q3
    T -->|создаёт| Q4

    Q4 -.->|внешний ответ: Q415638, P274=NTi| W["Wikidata"]
```

## Соответствие заметкам

- Источники: `notes/Review-W2587989553.md`, `notes/Review-W2344885033.md`, `notes/Review-W2590450430.md`, `notes/Review-W4367393972.md`, `notes/Review-W4388628377.md`.
- Запросы: `notes/Query-OpenAlex-PLAL.md`, `notes/Query-Targeted-1.md`, `notes/Query-Targeted-2.md`, `notes/Query-Wikidata-TiN.md`.
- Задача: `tasks/Task-Literature-Session-2.md`.
- Метод: `notes/Literature-Extraction.md` (существующая заметка).

## Оговорки

- `Query-Wikidata-TiN` не порождает новый источник в `reviews.json`; это отдельная проверка сущности TiN.
- Фактический тип графа OpenAlex у W2344885033 и W2590450430 — `article`, хотя по содержанию это обзоры. На схеме это не скрывается.
- Проверка студентом для всех новых заметок: pending.
