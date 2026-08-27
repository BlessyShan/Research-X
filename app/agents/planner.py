import json

from app.llm import ask_ai
from app.models.schemas import ResearchPlan


def clean_json_response(response):

    response = response.strip()

    if response.startswith("```"):

        lines = response.splitlines()

        lines = [
            line
            for line in lines
            if not line.strip().startswith("```")
        ]

        response = "\n".join(lines).strip()

    return response


def create_research_plan(topic: str) -> ResearchPlan:

    prompt = f"""
You are the Planning Agent of Research-X.

Research topic:
{topic}

Create a comprehensive research plan.

The plan must contain:

1. One research objective.
2. Exactly 6 research subtasks.
3. Each subtask must investigate a DIFFERENT aspect.
4. Each subtask must contain 3 specific search keywords.
5. Search keywords must NOT be repeated between subtasks.
6. Include appropriate source types.

Focus on academically useful and reliable research.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "objective": "string",

    "subtasks": [
        {{
            "title": "string",
            "investigation": "string",

            "search_keywords": [
                "specific search query 1",
                "specific search query 2",
                "specific search query 3"
            ],

            "source_types": [
                "string",
                "string"
            ]
        }}
    ]
}}
"""

    response = ask_ai(prompt)

    response = clean_json_response(response)

    try:

        data = json.loads(response)

        return ResearchPlan(**data)

    except Exception as e:

        raise ValueError(
            f"Planner returned invalid research plan: {e}"
        )