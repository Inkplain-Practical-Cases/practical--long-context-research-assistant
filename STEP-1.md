# STEP-1 of 6 — Research query and document intake

## What you build
A FastAPI request boundary receives a research question and up to five documents, rejects invalid payloads, and returns a deterministic receipt with a UUID and document counts. The in-memory provider makes this step runnable without cloud services.

## Architecture
`submit_research` (door) → `handle_intake` (handler) → `service_intake` (service) → `MemoryResearchRepository.save` (provider). Pydantic models validate data before the handler executes.

## Run and verify
`python -m pip install -r requirements.txt` then `python -m pytest -q`; run `uvicorn app.main:app --reload` for manual API checks.

## Security boundary
`tenant_id` is a **caller-supplied label**, not authenticated identity. Do not expose this step to untrusted users. Real identity and per-tenant authorization must be added before any cross-tenant retrieval feature.

## Next
STEP-2 adds session/document memory boundaries and read authorization.
