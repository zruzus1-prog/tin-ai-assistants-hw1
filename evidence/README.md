# Журналы и проверки

- `runs/`, `prompts/`, `run_summary.json` — постановки, события, ответы,
  вызовы инструментов, ошибки, токены и идентификаторы сессий.
- `ai4science_*` — действительные прогоны учебной среды.
- `research_api_calls.jsonl` — ответы OpenAlex и Wikidata без ключей.
- `publisher_verification.json`, `thesis_verification.json` — сверка источников.
- `checker_negative_cases.json`, `guard_probe.json` — отрицательные проверки.
- `final_verification.json` — итоговая проверка сохранённых артефактов.

Локальные пути нормализованы; события и результаты экспериментов сохранены.
Подтверждения студента записаны отдельно в `student_review.json`.
