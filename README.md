# Long-Context Research Assistant

Six cumulative teaching branches; STEP-1 implements a typed research intake API with a deterministic in-memory repository. This is **not** yet a long-context inference engine or production authorization layer.

Run: `python -m pip install -r requirements.txt`, `python -m pytest -q`, `uvicorn app.main:app --reload`. Submit POST `/research` with a tenant_id, question, and 1–5 title/text documents. Use synthetic data only.
