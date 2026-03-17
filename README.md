# Market Analysis API (India Sectors)

A FastAPI-based backend service that analyzes Indian market sectors and generates structured trade opportunity reports using AI and market data.

---

## Features

* Sector-based analysis (technology, pharma, agriculture, etc.)
* AI-powered insights using Google Gemini API
* Market data collection (news/trends)
* API key authentication
* Rate limiting (per user)
* Session tracking (in-memory)
* Markdown report generation
* Auto API documentation (Swagger UI)

---

## Tech Stack

* FastAPI
* Python
* Google Gemini API
* HTTPX
* Pydantic
* Python-dotenv

---

## Project Structure

```
APPSCRIP ASSIGNMENT/
│
├── app/
│   ├── core/
│   │   ├── rate_limit.py
│   │   ├── security.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── schema.py
│   │
│   ├── routes/
│   │   └── analyze.py
│   │
│   ├── services/
│   │   ├── ai.py
│   │   ├── report.py
│   │   └── search.py
│   │
│   └── main.py
│
├── .env
├── requirements.txt
└── venv/
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd APPSCRIP ASSIGNMENT
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in root:

```
GEMINI_API_KEY=your_gemini_api_key
API_KEY=secret123
```

---

### 5. Run the server

```
uvicorn app.main:app --reload
```

---

## API Usage

### Endpoint

```
GET /analyze/{sector}
```

---

### Example Request

```
curl -H "x-api-key: secret123" \
http://127.0.0.1:8000/analyze/technology
```

---

### Example Response

```
{
  "report": "# Market Analysis: Technology (India)\n\n## Current Trends\n...\n\n## Opportunities\n...\n\n## Risks\n...\n\n## Trade Ideas\n..."
}
```

---

## Security Features

* API Key Authentication (`x-api-key`)
* Input Validation using Pydantic
* Rate Limiting (5 requests/minute per API key)
* Environment-based secret management

---

## Core Workflow

1. Accept sector input
2. Validate input
3. Authenticate user
4. Apply rate limiting
5. Fetch market data/news
6. Analyze using Gemini API
7. Generate structured markdown report
8. Return response

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Error Handling

* Handles invalid sector input
* Handles external API failures
* Returns proper HTTP error responses

---

## Assignment Criteria Covered

* FastAPI implementation with async support
* AI integration (Gemini API)
* Market data collection
* Authentication and rate limiting
* Clean modular architecture
* Structured markdown output
* Proper error handling

---
