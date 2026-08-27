import requests
from bs4 import BeautifulSoup


def read_webpage(url: str) -> str:

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for element in soup(
        ["script", "style", "nav", "footer", "header"]
    ):
        element.decompose()

    text = soup.get_text(
        " ",
        strip=True
    )

    return text[:12000]