# GuardAgent Setup

## Tạo Virtual Environment

python -m venv .venv

## Activate (Windows)

.venv\Scripts\activate

## Cài FastAPI

pip install fastapi

## Cài Uvicorn

pip install "uvicorn[standard]"

## Lưu dependencies

pip freeze > requirements.txt

## Cài lại dependencies

pip install -r requirements.txt

## Kiểm tra package

pip list
