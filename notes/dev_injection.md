### Detect-leakage

## What does this function do?

This function detects whether a text contains a prompt injection.

## What is the input?

A text string.

## What is the output?

A boolean value.

- True -> prompt injection detected.

- False -> No prompt injection detected.

## How does it work?

This function uses a for loop and the in operator to check whether the input contains any prompt injection keywords.

If a match is found, it returns True.

Otherwise, it returns False.

## How can you improve it?

- Add more prompt injection keywords.

- Detect prompt injection from multiple AI providers.

- Return more detailed detection results instead of only True or False.
