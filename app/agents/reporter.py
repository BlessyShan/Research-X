from datetime import datetime


def generate_report(
    topic,
    analysis,
    verification
):

    report = []

    report.append(
        "# Research-X Research Report\n"
    )

    report.append(
        f"## Topic\n{topic}\n"
    )

    report.append(
        f"Generated: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    )

    report.append(
        "## Executive Summary\n"
    )

    for finding in analysis["findings"][:5]:

        report.append(
            f"- {finding['claim']}\n"
        )

    report.append(
        "\n## Key Findings\n"
    )

    for index, finding in enumerate(
        analysis["findings"],
        start=1
    ):

        report.append(
            f"### {index}. "
            f"{finding['claim']}\n"
        )

        report.append(
            f"{finding['evidence']}\n"
        )

        report.append(
            f"**Confidence:** "
            f"{finding['confidence']}\n"
        )

        report.append(
            f"**Sources:**\n"
        )

        for url in finding["sources"]:

            report.append(
                f"- {url}\n"
            )

    report.append(
        "\n## Verification\n"
    )

    for item in verification:

        report.append(
            f"### {item['claim']}\n"
        )

        report.append(
            f"**Status:** "
            f"{item['status']}\n\n"
        )

        report.append(
            f"**Reason:** "
            f"{item['reason']}\n"
        )

    report.append(
        "\n## Agreements\n"
    )

    for item in analysis.get(
        "agreements",
        []
    ):

        report.append(
            f"- {item}\n"
        )

    report.append(
        "\n## Contradictions\n"
    )

    for item in analysis.get(
        "contradictions",
        []
    ):

        report.append(
            f"- {item}\n"
        )

    report.append(
        "\n## Limitations\n"
    )

    for item in analysis.get(
        "limitations",
        []
    ):

        report.append(
            f"- {item}\n"
        )

    report.append(
        "\n## Sources\n"
    )

    seen = set()

    for finding in analysis["findings"]:

        for url in finding["sources"]:

            if url not in seen:

                report.append(
                    f"- {url}\n"
                )

                seen.add(url)

    return "\n".join(report)