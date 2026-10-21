# Литература: итог поиска и проверки

[порождено] Дата: 20.10.2026. Тема обзора — лазерный синтез/обработка наночастиц: PLAL и общие механизмы. Набор шире TiN и не выдаётся за пять обзоров исключительно о TiN.

## Итоговые пять источников

| OpenAlex | Название | Год графа | Цитирований | DOI |
|---|---|---|---|---|
| W2587989553 | Laser Synthesis and Processing of Colloids: Fundamentals and Applications | 2017 | 1338 | [10.1021/acs.chemrev.6b00468](https://doi.org/10.1021/acs.chemrev.6b00468) |
| W2344885033 | Synthesis of Nanoparticles by Laser Ablation: A Review | 2016 | 480 | [10.14356/kona.2017009](https://doi.org/10.14356/kona.2017009) |
| W2590450430 | External field-assisted laser ablation in liquid: An efficient strategy for nanocrystal synthesis and nanostructure assembly | 2017 | 352 | [10.1016/j.pmatsci.2017.02.004](https://doi.org/10.1016/j.pmatsci.2017.02.004) |
| W4367393972 | Effect of Liquid and Laser Parameters on Fabrication of Nanoparticles via Pulsed Laser Ablation in Liquid with Their Applications: A Review | 2023 | 55 | [10.1007/s11468-023-01852-7](https://doi.org/10.1007/s11468-023-01852-7) |
| W4388628377 | Fabrication of Au–Ag Bimetallic Nanoparticles Using Pulsed Laser Ablation for Medical Applications: A Review | 2023 | 35 | [10.3390/nano13222940](https://doi.org/10.3390/nano13222940) |

Источники отсортированы по cited_by в отобранном тематическом наборе. Это не доказательство исчерпывающего мирового топ-5: полнота OpenAlex и классификация жанра ограничены. KONA — общий обзор лазерной абляции с акцентом на газовую среду, а не прямой источник условий PLAL.

## Как получен набор

Сначала использовался research_openalex_search: 2016–2026, type=review, сортировка по цитированиям. Высокая цитируемость не спасала выдачу от нерелевантных работ. Повторный отбор убрал обзоры dewetting и плавления; нагрев/плавление и фрагментация разведены как разные режимы.
Затем по библиографии реальной страницы Plasmonics найдены три кандидата и выполнены точные поиски их названий с work_type=any и отдельные openalex_work. Это выявило обзоры, которые OpenAlex помечает как article. DOI, IDs, авторы и счётчики получены из настоящих ответов API, а не по памяти.

История запросов и выбранные IDs: library/query_notes.json, targeted_queries.json. Неотредактированные ответы без секретов: evidence/research_api_calls.jsonl. Действительные вызовы агента: evidence/runs/07_research_mcp, 09_review_refinement, 12_targeted_reviews.

## Независимая сверка издателей

Проверял ИИ, отдельно от авторского сеанса DeepSeek. Это проверка библиографических полей, а не чтение всех обзоров целиком и не собственная проверка студента.

- [W2587989553](https://pubs.acs.org/doi/10.1021/acs.chemrev.6b00468): publisher_check_incomplete. 

- [W2344885033](https://www.jstage.jst.go.jp/article/kona/34/0/34_2017009/_article): matched_publisher. OpenAlex publication year 2016; publisher issue 34 (2017), pages 80–90. The captured page metadata says online 2017/02/28. The cause of 2016 in OpenAlex was not established; do not automatically explain it as advance publication. Title identifies the work as a review; OpenAlex type remains article.

- [W2590450430](https://www.sciencedirect.com/science/article/pii/S0079642517300269): matched_publisher. OpenAlex type=article, while the work is presented as a review in title/abstract; no silent change of the graph field. Publisher abstract explicitly calls the work a review, while OpenAlex type is article.

- [W4367393972](https://link.springer.com/article/10.1007/s11468-023-01852-7): matched_publisher. Publisher has a public abstract, although OpenAlex abstract is absent. Absence in the graph is not absence at the publisher.

- [W4388628377](https://www.mdpi.com/2079-4991/13/22/2940): matched_publisher. No bibliographic mismatch found in the checked fields.

Прямые HTTP-запросы к части издателей упирались в 403/страницы проверки клиента. KONA проверен по метаданным страницы; Springer — по странице, открытой поисковым инструментом; Elsevier и MDPI — по индексированным страницам самих издателей. Эти способы и исходные HTTP-статусы сохранены, сетевой отказ не скрыт. Crossref использован дополнительным независимым реестром, а не назван издателем.

## Wikidata и SPARQL

Действительный wikidata_search("titanium nitride", en) вернул Q415638. Затем выполнен read-only SELECT с OPTIONAL для P31 и P274: P31=Q113145171 (type of chemical entity), P274=NTi. Порядок элементов сохранён как внешний ответ; это не ручное изменение формулы в базе.
Точный запрос, дата и JSON ответа сохранены в аудите и notes/Query-Wikidata-TiN.md. В запросе нет команд изменения данных.

## Подтверждения проверки

В `student_review.json` сохранены подтверждения сверки W2587989553,
W2344885033 и W2590450430. Они отделены от результатов автоматической
проверки выше: отказ HTTP 403 не переименован в успешный автоматический запрос.
