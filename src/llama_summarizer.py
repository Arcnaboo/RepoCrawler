import os
from dotenv import load_dotenv
import requests

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = """
You are ArcInspect, a senior AI engineer analyzing source code.

Your job:
- Read a file.
- Summarize what it does in one sentence.
- Then list key classes or functions, and what they do.

Respond clearly in markdown format.
"""

def summarize_code(path, content):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"[FILE: {path}]\n\n{content[:3000]}"}
    ]

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": messages,
        "temperature": 0.2
    }

    response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)

    if not response.ok:
        raise Exception(f"Groq API Error: {response.status_code} - {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()
