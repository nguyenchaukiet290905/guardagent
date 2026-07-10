# process_agent_request

## What does this function do?

This function checks whether a text string from dictionary contains a prompt injection keywords.

## What is the input?

A text string.

## What is the output?

A text string.

match là kết quả trả về từ detect_injection(content)

- True -> Phát hiện prompt injection
- False -> Không phát hiện prompt injection


## How does it work?

This function uses a json.loads and data["content"] to check whether the input contains any prompt injection keywords.

detect_injection(content) trả về

-True -> Có prompt injection
- False -> Không có prompt injection

- Nếu match = True thì process_agent_request() trả về 
"Tu choi thong bao."

- Nếu match = False thì process_agent_request() trả về  
"Thong bao hop le."

## How can you improve it?

- Support more json formats.

- Return more detailed detection results instead of only Tu choi thong bao or Thong bao hop le.
