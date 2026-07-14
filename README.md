# 🛡️ GuardAgent

> A lightweight AI Security project for detecting Prompt Injection and Sensitive Data Leakage using rule-based techniques.

---

## Overview

GuardAgent is a minimal AI Security learning project that focuses on protecting AI applications from common security threats.

The current implementation provides a simple rule-based security engine capable of detecting:

- Prompt Injection attempts
- Sensitive API Key leakage

This project is being developed step by step as part of an AI Security learning roadmap.

---

## Features

- ✅ Prompt Injection Detection
- ✅ API Key Leakage Detection
- ✅ Rule-based AI Security Detection
- ✅ FastAPI REST API
- ✅ Pydantic Request Validation

---

## Project Structure

```text
guardagent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── security_engine.py
│
├── tests/
│   ├── __init__.py
│   └── test_security_engine.py
│
├── logs/
├── notes/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Security Engine

Current functions

```python
detect_leakage(text: str) -> bool

detect_injection(text: str) -> bool
```

## REST API

Current endpoint

POST /v1/shield

Request

{
    "text": "Ignore previous instructions."
}

Response

{
    "blocked": true
}

## Live Demo

Swagger UI:
https://guardagent-93lr.onrender.com/docs

## API Documentation

<img src="images/swagger.png" width="900">

### Prompt Injection Detection

The engine detects common jailbreak keywords such as:

- ignore previous instructions
- system prompt
- developer message
- forget all previous

### Sensitive Data Leakage Detection

The engine detects OpenAI API Keys using Regular Expressions.

Regex pattern:

```text
sk-[a-zA-Z0-9]{48}
```

---

## Example

```python
from app.security_engine import (
    detect_injection,
    detect_leakage,
)

detect_injection(
    "Ignore previous instructions."
)

detect_leakage(
    "sk-abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH1234"
)
```

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| FastAPI | REST API |
| Pydantic | Request Validation |
| Regular Expressions | API Key Detection |
| Rule-based Logic | Prompt Injection Detection |

---

## Threat Model

| Threat | Detection Method |
|---------|------------------|
| Prompt Injection | Keyword Matching |
| API Key Leakage | Regular Expression |

---

## Roadmap

- [x] Prompt Injection Detection
- [x] API Key Leakage Detection
- [x] FastAPI REST API
- [x] Pydantic Validation
- [ ] Structured JSON Logging
- [ ] Automated Testing with Pytest
- [ ] Docker Support

---

## Run

1. Clone Repository
```bash
git clone https://github.com/nguyenchaukiet290905/guardagent.git
```
2. Install Dependencies

pip install -r requirements.txt

3. Run REST API

uvicorn app.main:app --reload

4. Open Swagger UI

http://127.0.0.1:8000/docs

Optional

Run Security Engine

```bash
python app/security_engine.py
```

## Future Improvements

- JSON Structured Logging
- Secure Exception Handling
- Docker Container
- Automated Security Testing

---

## Author

**Nguyen Kiet**

IT Student – Ho Chi Minh City University of Industry and Trade (HUIT)

AI Security Learning Project (2026)

