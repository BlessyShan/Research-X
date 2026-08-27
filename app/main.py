import os

from app.agents.planner import create_research_plan
from app.agents.researcher import research_task
from app.agents.analyzer import analyze_sources
from app.agents.verifier import verify_findings
from app.agents.reporter import generate_report


def main():

    print("\n")
    print("=" * 70)
    print("                    RESEARCH-X")
    print("              AUTONOMOUS RESEARCH AGENT")
    print("=" * 70)

    topic = input(
        "\nWhat would you like to research?\n> "
    )

    # --------------------------------------------------
    # PLANNER
    # --------------------------------------------------

    print("\n🧠 Creating research plan...")

    plan = create_research_plan(topic)

    print(
        f"✓ Created {len(plan.subtasks)} research subtasks."
    )

    # --------------------------------------------------
    # RESEARCH
    # --------------------------------------------------

    all_sources = []

    for index, task in enumerate(
        plan.subtasks,
        start=1
    ):

        print(
            f"\n🔎 Researching "
            f"{index}/{len(plan.subtasks)}: "
            f"{task.title}"
        )

        task_data = {
            "title": task.title,
            "investigation": task.investigation,
            "search_keywords": task.search_keywords,
            "source_types": task.source_types
        }

        sources = research_task(
            task_data
        )

        all_sources.extend(
            sources
        )

        unique_sources = {}
        for source in all_sources:
            unique_sources[source["url"]] = source
            all_sources = list(
                unique_sources.values()
            )
            print(
                f"\n📚 Unique sources collected: "
                f"{len(all_sources)}"
            )
        print(
            f"✓ Collected "
            f"{len(sources)} sources"
        )

    # --------------------------------------------------
    # GLOBAL SOURCE DEDUPLICATION
    # --------------------------------------------------

    unique_sources = []

    seen_urls = set()

    for source in all_sources:

        url = source.get(
            "url",
            ""
        ).strip()

        if not url:
            continue

        if url in seen_urls:
            continue

        seen_urls.add(url)

        unique_sources.append(
            source
        )

    all_sources = unique_sources

    print(
        f"\n📚 Unique sources collected: "
        f"{len(all_sources)}"
    )

    # --------------------------------------------------
    # SAFETY CHECK
    # --------------------------------------------------

    if not all_sources:

        print(
            "\n❌ Research failed: "
            "No sources were collected."
        )

        return

    # --------------------------------------------------
    # ANALYSIS
    # --------------------------------------------------

    print(
        "\n🧠 Analyzing evidence..."
    )

    analysis = analyze_sources(
        topic,
        all_sources
    )

    print(
        "✓ Evidence analyzed"
    )

    # --------------------------------------------------
    # VERIFICATION
    # --------------------------------------------------

    print(
        "\n🔍 Verifying findings..."
    )

    verification = verify_findings(
        analysis["findings"]
    )

    print(
        "✓ Findings verified"
    )

    # --------------------------------------------------
    # REPORT
    # --------------------------------------------------

    print(
        "\n📝 Generating final report..."
    )

    report = generate_report(
        topic,
        analysis,
        verification
    )

    os.makedirs(
        "data/reports",
        exist_ok=True
    )

    filename = (
        "data/reports/"
        + topic.lower()
        .replace(" ", "_")
        .replace("/", "_")
        + ".md"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("\n")
    print("=" * 70)
    print("                  RESEARCH COMPLETE")
    print("=" * 70)

    print(
        f"\n📄 Report saved to:\n{filename}"
    )

    print("\n")


if __name__ == "__main__":
    main()