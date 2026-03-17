import os
import httpx
from dotenv import load_dotenv

# Load env variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def analyze_with_gemini(sector: str, news_data: list):
    if not GEMINI_API_KEY:
        return "Missing Gemini API Key"

    prompt = f"""
    You are a financial analyst.

    Analyze the {sector} sector in India using the data below.

    Return structured output with headings:
    - Current Trends
    - Opportunities
    - Risks
    - Trade Ideas

    Data:
    {news_data}
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.post(url, json=payload)

    if response.status_code != 200:
        return f"Gemini API Error: {response.text}"

    data = response.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "Error generating AI response"