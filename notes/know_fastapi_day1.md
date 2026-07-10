# FastAPI Day 1

FastAPI là framework xây REST API.

app = FastAPI()
-> Tạo ứng dụng.

@app.get("/")
-> Khi client gửi GET / thì gọi function.

@app.post("/v1/shield")
-> Khi client gửi POST /v1/shield thì gọi function.

uvicorn app.fastapi_demo:app --reload
-> Chạy server
công thức: app là thư mục, fastapi_demo là tên file
app thứ 2 là biến app = FastAPI() tạo ứng dụng

Công thức:

uvicorn <module>:<app_instance> --reload

http://127.0.0.1:8000/docs
-> Swagger UI để test API
-> Trình duyệt mặc định chỉ gửi GET khi nhập URL, nên
muốn test POST thì dùng Swagger hoặc Postman.