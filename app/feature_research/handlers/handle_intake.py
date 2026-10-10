"""Handler delegates intake without embedding storage or HTTP concerns."""
from app.contracts.research import ResearchIntake, ResearchReceipt
from app.providers.memory_research import MemoryResearchRepository
from app.feature_research.services.service_intake import service_intake

def handle_intake(intake: ResearchIntake, repository: MemoryResearchRepository) -> ResearchReceipt:
    return service_intake(intake, repository)
