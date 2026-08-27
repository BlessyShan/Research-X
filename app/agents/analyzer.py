import json

from app.llm import ask_ai


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


def analyze_batch(
    topic,
    sources,
    batch_number
):

    source_text = ""

    for index, source in enumerate(
        sources,
        start=1
    ):

        source_text += f"""
SOURCE {index}

Title:
{source['title']}

URL:
{source['url']}

Content:
{source['content'][:5000]}

--------------------------------------------------
"""

    prompt = f"""
You are the Analysis Agent in Research-X.

Research topic:
{topic}

You are analyzing research evidence batch {batch_number}.

Analyze ONLY the sources provided below.

{source_text}

Identify important factual claims supported by the sources.

For each claim:

- State the claim clearly.
- Explain the evidence.
- Include the URLs supporting the claim.
- Assign confidence between 0.0 and 1.0.

Do not invent information.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "findings": [
        {{
            "claim": "string",
            "evidence": "string",
            "sources": ["URL"],
            "confidence": 0.0
        }}
    ],

    "agreements": [
        "string"
    ],

    "contradictions": [
        "string"
    ],

    "limitations": [
        "string"
    ]
}}
"""

    response = ask_ai(
        prompt
    )

    response = clean_json_response(
        response
    )

    return json.loads(
        response
    )


def analyze_sources(
    topic,
    sources
):

    # Keep Gemini prompts manageable
    batch_size = 12

    all_findings = []
    all_agreements = []
    all_contradictions = []
    all_limitations = []

    batches = [
        sources[i:i + batch_size]
        for i in range(
            0,
            len(sources),
            batch_size
        )
    ]

    print(
        f"📦 Analyzing "
        f"{len(sources)} sources "
        f"in {len(batches)} batches..."
    )

    for index, batch in enumerate(
        batches,
        start=1
    ):

        print(
            f"   → Analysis batch "
            f"{index}/{len(batches)}"
        )

        try:

            result = analyze_batch(
                topic,
                batch,
                index
            )

            all_findings.extend(
                result.get(
                    "findings",
                    []
                )
            )

            all_agreements.extend(
                result.get(
                    "agreements",
                    []
                )
            )

            all_contradictions.extend(
                result.get(
                    "contradictions",
                    []
                )
            )

            all_limitations.extend(
                result.get(
                    "limitations",
                    []
                )
            )

        except Exception as e:

            print(
                f"⚠️ Batch {index} "
                f"analysis failed: {e}"
            )

    # Remove duplicate text entries
    all_agreements = list(
        dict.fromkeys(
            all_agreements
        )
    )

    all_contradictions = list(
        dict.fromkeys(
            all_contradictions
        )
    )

    all_limitations = list(
        dict.fromkeys(
            all_limitations
        )
    )

    return {
        "findings": all_findings,
        "agreements": all_agreements,
        "contradictions": all_contradictions,
        "limitations": all_limitations
    }