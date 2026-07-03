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
- ✅ Rule-based Detection Engine
- ✅ Regex-based Pattern Matching

---

## Project Structure

```text
guardagent/
│
├── app/
│   ├── __init__.py
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
| Python 3.13+ | Core Programming Language |
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
- [ ] FastAPI Integration
- [ ] Pydantic Validation
- [ ] Structured JSON Logging
- [ ] Automated Testing with Pytest
- [ ] Docker Support

---

## Run

Clone the repository

```bash
git clone https://github.com/<your-github-username>/guardagent.git
```

Move into the project

```bash
cd guardagent
```

Run the application

```bash
python app/security_engine.py
```

---

## Future Improvements

- FastAPI REST API
- JSON Structured Logging
- Secure Exception Handling
- Docker Container
- Automated Security Testing

---

## Author

**Nguyen Kiet**

IT Student – Ho Chi Minh City University of Industry and Trade (HUIT)

AI Security Learning Project (2026)