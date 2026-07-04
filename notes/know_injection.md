### Detect-Injection

## What is Keyword Matching

Keyword Matching is a technique that detects specific words or phrases in text.

## Why do we use Keyword Matching

Prompt Injection does not have a fixed format like an API key.

Instead, we check whether the input contains suspicious keywords.

## What is Prompt Injection

Prompt Injection is an attack that tricks an AI model into ignoring its original instructions and following the attacker's instructions.

## Why do we use Injection

We detect prompt injection to protect AI systems from malicious user input.

## Example

[] -> list

Ignore the previous

go to the system

## In my code

keywords =[
    "Ignore the previous",
    "go to the system"
]
for keyword in keywords:
    if keyword in text
        return true
    return false

This for loop checks each keyword in the list.

If a keyword is found in the input text, the function returns True.

Otherwise, it returns False.
