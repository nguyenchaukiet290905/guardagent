### Detect-leakage

## What does this function do?

This function detects whether a text contains an OpenAI API key.

## What is the input?

A text string.

## What is the output?

A boolean value.

- True -> API key detected.

- False -> No API key detected.

## How does it work?

This Function uses a Regular Expression (Regex) to search for an API key pattern.

If a match is found, it returns True.

Otherwise, it returns False.

## How can you improve it?

- Support more API key formats.

- Detect API keys from multiple AI providers.

- Return more detailed detection results instead of only True or False.
