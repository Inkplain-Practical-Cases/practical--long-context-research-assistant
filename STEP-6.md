# Orchestrate bounded multi-document research

Run python -m pytest -q. The implementation is an offline deterministic reference, not an external LLM integration.

## Database (Entity) Relations
STEP-6 records research API HTTP request metadata and outcome events in SQLite (no document bodies). See STEP-6.erd and STEP-6-ERD.
