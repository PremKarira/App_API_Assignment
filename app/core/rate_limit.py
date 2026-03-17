import time

requests_log = {}

LIMIT = 5
WINDOW = 60  # seconds

def rate_limiter(api_key: str):
    now = time.time()

    if api_key not in requests_log:
        requests_log[api_key] = []

    requests_log[api_key] = [
        t for t in requests_log[api_key] if now - t < WINDOW
    ]

    if len(requests_log[api_key]) >= LIMIT:
        raise Exception("Rate limit exceeded")

    requests_log[api_key].append(now)