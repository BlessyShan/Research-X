from typing import List

from pydantic import BaseModel


class ResearchSubtask(BaseModel):

    title: str

    investigation: str

    search_keywords: List[str]

    source_types: List[str]


class ResearchPlan(BaseModel):

    objective: str

    subtasks: List[ResearchSubtask]


class Source(BaseModel):

    title: str

    url: str

    source_type: str

    query: str

    content: str

    relevance: float = 0.0


class ResearchFinding(BaseModel):

    claim: str

    evidence: str

    sources: List[str]

    confidence: float = 0.0