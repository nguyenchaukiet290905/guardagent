# AI Security Notes

## Detection Techniques

| Threat | Technique |
|---------|-----------|
| API Key Leakage | Regex |
| Prompt Injection | Keyword Matching |

---

## Regex

Purpose:
- Detect text with a fixed format.

Examples:
- API Keys
- Email
- IP Address
- Phone Number

Python:
re.search(pattern, text)

---

## Keyword Matching

Purpose:
- Detect suspicious words or phrases.

Python:

for keyword in keywords:
    if keyword in text:
        return True

---

## Current GuardAgent Modules

- detect_leakage()
- detect_injection()

---

## Things I Learned

- Regex is good for fixed patterns.
- Prompt Injection has no fixed pattern.
- Keyword Matching is simple but effective.
- Return type: bool