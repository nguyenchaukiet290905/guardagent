# Detect Leakage

## Regex là gì?

Regex (Regular Expression) là một công cụ dùng để tìm kiếm hoặc kiểm tra chuỗi theo một mẫu (pattern) xác định.

## Tại sao dùng Regex?

API Key có định dạng cố định.

Regex giúp phát hiện API Key tự động mà không cần kiểm tra từng ký tự.

## Ví dụ

[] → Nhóm ký tự (Character Class)

[a-z] → Chữ thường

[A-Z] → Chữ hoa

[0-9] → Chữ số

{48} → Chính xác 48 ký tự

## Trong code của mình

pattern = r"sk-[a-zA-Z0-9]{48}"

Pattern này dùng để tìm OpenAI API Key.

re.search(pattern, text)

Hàm này tìm pattern trong chuỗi text.

Nếu tìm thấy → trả về Match Object.

Nếu không tìm thấy → trả về None.