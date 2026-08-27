from app.tools.web_search import search_web
from app.tools.webpage_reader import read_webpage


def research_task(task, max_queries=2):

    queries = task.get(
        "search_keywords",
        []
    )

    if not queries:

        queries = [
            task["investigation"],
            f"{task['title']} research study"
        ]

    all_sources = []

    for query in queries[:max_queries]:

        print(
            f"\n🌐 Searching: {query}"
        )

        results = search_web(
            query,
            max_results=3
        )

        for result in results:

            try:

                content = read_webpage(
                    result["url"]
                )

            except Exception:

                content = result.get(
                    "snippet",
                    ""
                )

            all_sources.append({
                "title": result["title"],
                "url": result["url"],
                "query": query,
                "content": content
            })

    return all_sources