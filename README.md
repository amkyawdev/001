# AI Chat Bot

A chatbot powered by **Groq LLM (llama3-70b)**, built with **FastAPI** (backend) and **Vue 3** (frontend). Deployable to Vercel.

## Stack

| Layer    | Tech |
|----------|------|
| Backend  | Python · FastAPI |
| AI Model | Groq · llama3-70b-8192 |
| Frontend | Vue 3 · Vite · Axios |
| Deploy   | Vercel |

## Deploy to Vercel

1. Go to [vercel.com](https://vercel.com) → **New Project** → Import this repo
2. In **Environment Variables**, add: `GROQ_API_KEY` = your key from [console.groq.com](https://console.groq.com)
3. Click **Deploy**

## Run Locally

```bash
# Backend
cd backend
pip install -r requirements.txt
GROQ_API_KEY=your_key uvicorn api.index:app --reload --port 8000

# Frontend (new terminal)
cd frontend
npm install && npm run dev
```

> Open http://localhost:5173
