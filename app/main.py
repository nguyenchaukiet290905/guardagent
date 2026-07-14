from fastapi import FastAPI
from app.security_engine import detect_injection
from pydantic import BaseModel

class ShieldRequest(BaseModel):
    text: str
    
app = FastAPI()
@app.post("/v1/shield")
async def shield(request: ShieldRequest):
    if detect_injection(request.text):
        return {
            "blocked": True
        }
    return {
        "blocked": False
    }