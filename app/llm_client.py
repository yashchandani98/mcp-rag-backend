import os
import requests

from dotenv import load_dotenv
load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "http://localhost",
    "X-Title": "mcp-rag-backend"
}
def generate_answer(prompt: str):
    payload = {
        "model": "openai/gpt-4o-mini",  # can swap anytime
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
