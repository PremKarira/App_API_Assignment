import httpx

async def fetch_news(sector: str):
    query = f"{sector} sector India news"
    url = "https://duckduckgo.com/?q=" + query

    # Simple placeholder (since scraping fully takes time)
    # You can improve later
    return [
        f"{sector} sector is growing in India",
        f"New policies impacting {sector}",
        f"Investment trends in {sector}"
    ]