from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from app.core.security import verify_api_key
from app.core.rate_limit import rate_limiter
from app.services.search import fetch_news
from app.services.ai import analyze_with_gemini
from app.services.report import generate_markdown
import markdown

router = APIRouter()

@router.get("/analyze/{sector}", response_class=HTMLResponse)
async def analyze_sector(
    sector: str,
    api_key: str = Depends(verify_api_key)
):
    # Rate limit
    rate_limiter(api_key)

    # Input validation
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")

    try:
        news_data = await fetch_news(sector)
        ai_output = await analyze_with_gemini(sector, news_data)
        report_md = generate_markdown(sector, ai_output)

        # Convert markdown → HTML
        report_html = markdown.markdown(report_md)

        # Styled HTML page
        html_content = f"""
        <html>
        <head>
            <title>{sector.title()} Analysis</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 900px;
                    margin: auto;
                    padding: 20px;
                    line-height: 1.6;
                    background-color: #f9f9f9;
                }}
                h1, h2 {{
                    color: #2c3e50;
                }}
                h1 {{
                    border-bottom: 2px solid #ddd;
                    padding-bottom: 10px;
                }}
                pre {{
                    background: #f4f4f4;
                    padding: 10px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            {report_html}
        </body>
        </html>
        """

        return HTMLResponse(content=html_content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))