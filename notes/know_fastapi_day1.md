# FastAPI Day 1

FastAPI là framwork xây REST API.

app = FastAPI()
-> Tạo ứng dụng.

@app.get("/")
-> Khi cilent gửi GET / thì gọi function.

@app.post("/v1/shield")
-> Khi cilent gửi POST /v1/shield thì gọi function.

uvicorn app.fastapi_demo:app --reload
-> Chạy server
công thức: app là thư mục, fastapi_demo là tên file
app thứ 2 là biến app = FastAPI() tạo ứng dụng

http://127.0.0.1:8000/docs
-> Swagger UI để test API bởi vì POST thì ko gõ link như GET được.