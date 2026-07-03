# AI Security Notes

## Day 1 - Detect Leakage

### Core Idea

Sensitive data can be leaked accidentally.

Example:

* OpenAI API Key
* Password
* Token

### Regex

Regex is used to match text patterns.

Example:

sk-[a-zA-Z0-9]{48}

### What I Built

detect_leakage(text)

Returns:

* True → API Key detected
* False → Safe

### Security Insight

Rule-based detection is simple and practical.

Many security tools start with pattern matching.

### My Takeaway

GuardAgent uses Regex to detect leakage API keys before sending prompts to an LLM.




---

## Day 2 - Detect Injection

### Core Idea

Attackers may try to manipulate AI instructions.

Example:

* ignore previous instructions
* system prompt
* forget all previous

### Keyword Detection

Use:

* List
* For Loop
* in Operator

### What I Built

detect_injection(text)

Returns:

* True → Dangerous prompt detected
* False → Safe

### Security Insight

Prompt Injection is one of the most common LLM attacks.

Keyword matching is the first layer of defense.

### Improvement Idea

Convert input to lowercase before checking.

Example:

IgNoRe PrEvIoUs

↓

ignore previous
