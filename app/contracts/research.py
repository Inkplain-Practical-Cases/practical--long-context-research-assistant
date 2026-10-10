"""Typed intake contracts; these reject oversized and empty inputs before storage."""
from pydantic import BaseModel, Field, field_validator

class DocumentInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    text: str = Field(min_length=1, max_length=10000)

    @field_validator("text")
    @classmethod
    def reject_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Document text must contain non-whitespace content")
        return value

class ResearchIntake(BaseModel):
    tenant_id: str = Field(min_length=1, max_length=64, pattern=r"^[a-zA-Z0-9_-]+$")
    question: str = Field(min_length=3, max_length=500)
    documents: list[DocumentInput] = Field(min_length=1, max_length=5)

class ResearchReceipt(BaseModel):
    research_id: str
    tenant_id: str
    document_count: int
    total_characters: int
    status: str = "received"
