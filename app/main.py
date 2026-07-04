import json
from app.security_engine import detect_injection
from app.security_engine import detect_leakage

def process_agent_request(raw_json_str: str) -> str:
    try:
        data = json.loads(raw_json_str)
        content = data.get("content", "")
        match = detect_injection(content)
        if match:
            return "Thong bao tu choi"
        return "Thong bao hop le"
    except json.JSONDecodeError:
        return "Invalid JSON format"

