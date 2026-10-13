"""FastAPI composition root; keep business logic outside the door."""
from fastapi import FastAPI
from app.feature_research.router import router

app = FastAPI(title="Long-Context Research Assistant — STEP-1")
app.include_router(router)

# Persist limited HTTP audit metadata through an independent adapter.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
