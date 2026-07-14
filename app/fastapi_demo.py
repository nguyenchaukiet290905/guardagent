from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {
        "message": "Hello GuardAgent"
    }

@app.post("/v1/shield")
async def shield():
    return {
        "blocked": True
    }    