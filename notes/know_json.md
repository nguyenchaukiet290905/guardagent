# process_agent_request

## Json là gì?

JSON (Javascript Object Notation) là định dạng dữ liệu dạng text dùng để 
trao đổi dữ liệu giữa các hệ thống. Trong Python, JSON thường được parse thành dictionary bằng
json.loads()

## Tại sao dùng Json?

Vi json nó nhẹ hơn xml và nó không có nhìu cấu trúc <>, đơn giản, trực quan
- Chuẩn của REST API
- Người đọc dễ
- Máy xử lý nhanh
- Hầu hết AI API đều dùng JSON

## Ví dụ

{
    "content" : "hello"
}

raw_json_str
↓
'{"content":"hello"}'
↓
data["content"]
↓
"hello"

## Trong code của mình

data = json.loads(raw_json_str)
content = data["content"]
match = detect_injection(content)

Khi user viết {
    "content" : "hello"
}
thì json nó chỉ hiểu raw_json_str = '{
    "content" : "hello"
}'
sau đó qua hàm json.loads thì str này sẽ thành dictionary
tiếp theo data["content"] sẽ lấy value dựa trên key content trong dictionary
lúc này content đã có value
và hàm detect_injection(content) nó sẽ kiểm tra value của content có phải là prompt injection không
