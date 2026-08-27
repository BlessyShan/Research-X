from google import genai
from app.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_ai(prompt: str) -> str:

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print(
            f"❌ Gemini API error: {e}"
        )

        raise