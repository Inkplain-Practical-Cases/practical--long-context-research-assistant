"""Service calculates and persists the intake receipt through an injected repository."""
from app.contracts.research import ResearchIntake, ResearchReceipt
from app.providers.memory_research import MemoryResearchRepository

def service_intake(intake: ResearchIntake, repository: MemoryResearchRepository) -> ResearchReceipt:
    # The contract has already rejected blank and excessive input.
    return repository.save(intake)
