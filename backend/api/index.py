import sys
import os

# Allow importing from backend/core when Vercel runs this file
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from core.chat import get_bot_reply

app = FastAPI(title="ChatBot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class HistoryItem(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: Optional[List[HistoryItem]] = []


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/chat")
def chat(req: ChatRequest):
    history = [h.dict() for h in req.history] if req.history else []
    reply = get_bot_reply(req.message, history)
    return {"reply": reply}
