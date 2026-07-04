# Detect Injection

## Keyword Matching là gì?

Keyword Matching là kỹ thuật kiểm tra xem trong văn bản có chứa các từ khóa hoặc cụm từ đã định nghĩa trước hay không.

## Tại sao dùng Keyword Matching?

Prompt Injection không có định dạng cố định như API Key.

Vì vậy không thể dùng Regex.

Thay vào đó, ta kiểm tra xem input có chứa các từ khóa đáng ngờ hay không.

## Prompt Injection là gì?

Prompt Injection là kỹ thuật tấn công khiến AI bỏ qua hướng dẫn ban đầu và làm theo yêu cầu của kẻ tấn công.

## Tại sao phải phát hiện Prompt Injection?

Để bảo vệ hệ thống AI khỏi những yêu cầu độc hại của người dùng.

## Ví dụ

- Ignore previous instructions
- Forget everything above
- System prompt
- Developer message

## Trong code của mình

```python
keywords = [
    "Ignore previous instructions",
    "System prompt"
]

Chương trình sẽ duyệt từng keyword trong danh sách.

Nếu keyword xuất hiện trong input → trả về True.

Nếu không có keyword nào xuất hiện → trả về False.