import time

sessions = {}

def track_session(api_key: str):
    sessions[api_key] = {
        "last_access": time.time(),
        "count": sessions.get(api_key, {}).get("count", 0) + 1
    }