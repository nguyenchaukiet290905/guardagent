### Detect-Leakage

## What is Regex

Regex is a pattern used to detect API keys in text.

## Why do we use Regex

Regex helps detect API keys automatically.

## Example

[] -> Character class
[a-z] -> Lowercase letters
[A-Z] -> Uppercase letters
[0-9] -> Digits
{48} -> Exactly 48 characters

## In my code

pattern = r"[a-zA-Z0-9]{48}"

This pattern matches exactly 48 letters or digits.

re.search(pattern, text)

Searches for the pattern in the input text.
