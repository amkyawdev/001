import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = (
    "You are a helpful, friendly, and concise AI assistant. "
    "Answer clearly and naturally."
)

def get_bot_reply(user_message: str, history: list = None) -> str:
    """Call Groq LLM and return the assistant reply."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if history:
        for turn in history[-10:]:
            if turn.get("role") in ("user", "assistant"):
                messages.append({"role": turn["role"], "content": turn["content"]})

    messages.append({"role": "user", "content": user_message})

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )
    return completion.choices[0].message.content
