"""Deterministic in-memory storage for local teaching; never use as durable production storage."""
from uuid import uuid4
from app.contracts.research import ResearchIntake, ResearchReceipt

class MemoryResearchRepository:
    def __init__(self) -> None:
        # Separate entries by tenant; future steps will add identity verification.
        self._entries: dict[tuple[str, str], ResearchIntake] = {}

    def save(self, intake: ResearchIntake) -> ResearchReceipt:
        # UUID prevents accidental collisions across repeated submissions.
        research_id = str(uuid4())
        self._entries[(intake.tenant_id, research_id)] = intake
        return ResearchReceipt(
            research_id=research_id,
            tenant_id=intake.tenant_id,
            document_count=len(intake.documents),
            total_characters=sum(len(doc.text) for doc in intake.documents),
        )
