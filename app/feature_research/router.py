"""HTTP door validates typed input and injects the local repository."""
from fastapi import APIRouter, Depends
from app.contracts.research import ResearchIntake, ResearchReceipt
from app.feature_research.handlers.handle_intake import handle_intake
from app.providers.memory_research import MemoryResearchRepository

router = APIRouter()
_repository = MemoryResearchRepository()

def get_repository() -> MemoryResearchRepository:
    return _repository

@router.post("/research", response_model=ResearchReceipt, status_code=201)
def submit_research(intake: ResearchIntake, repository: MemoryResearchRepository = Depends(get_repository)) -> ResearchReceipt:
    # NOTE: tenant_id is untrusted input in STEP-1; authorization is not implemented yet.
    return handle_intake(intake, repository)
