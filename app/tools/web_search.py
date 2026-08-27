import requests
from bs4 import BeautifulSoup


def search_web(
    query: str,
    max_results: int = 5
):

    url = "https://html.duckduckgo.com/html/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        params={"q": query},
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    results = []

    for result in soup.select(
        ".result"
    )[:max_results]:

        title_element = result.select_one(
            ".result__title"
        )

        link_element = result.select_one(
            ".result__url"
        )

        snippet_element = result.select_one(
            ".result__snippet"
        )

        if not title_element or not link_element:
            continue

        title = title_element.get_text(
            " ",
            strip=True
        )

        link = link_element.get(
            "href"
        )

        snippet = ""

        if snippet_element:

            snippet = snippet_element.get_text(
                " ",
                strip=True
            )

        results.append({
            "title": title,
            "url": link,
            "snippet": snippet,
            "query": query
        })

    print(
        f"✓ Search returned "
        f"{len(results)} sources"
    )

    return results