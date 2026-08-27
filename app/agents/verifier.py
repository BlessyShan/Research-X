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


def verify_findings(findings):

    if not findings:

        return []

    findings_text = ""

    for index, finding in enumerate(
        findings,
        start=1
    ):

        findings_text += f"""
FINDING {index}

CLAIM:
{finding['claim']}

EVIDENCE:
{finding['evidence']}

SOURCE URLs:
{finding['sources']}

CONFIDENCE:
{finding.get('confidence', 0.0)}

--------------------------------------------------
"""

    prompt = f"""
You are the Verification Agent for Research-X.

Verify the following research findings.

{findings_text}

For each finding determine:

1. Whether the claim is supported by the evidence.
2. Whether the evidence is sufficiently strong.
3. Whether there is uncertainty or overclaiming.

Use ONLY the supplied evidence.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "verifications": [
        {{
            "claim": "string",
            "status": "VERIFIED",
            "reason": "short explanation",
            "sources": ["URL"]
        }}
    ]
}}

STATUS must be exactly one of:

VERIFIED
UNCERTAIN
UNSUPPORTED
"""

    response = ask_ai(prompt)

    response = clean_json_response(
        response
    )

    data = json.loads(response)

    return data.get(
        "verifications",
        []
    )