import requests
import json

API_KEY = "sk-or-v1-PASTE_YOUR_KEY_HERE"
MODEL = "meta-llama/llama-3.1-8b-instruct"

def interpret_command(user_command):
    prompt = f"""
You are an automation AI.
Convert the user command into JSON.

Allowed actions:
1. find_pdfs
2. move_pdfs

Respond ONLY with valid JSON.

Examples:
User: find all pdf in c drive
Output: {{ "action": "find_pdfs" }}

User: put all pdf in one single folder
Output: {{ "action": "move_pdfs", "folder": "All_PDFs" }}

User command:
{user_command}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "http://localhost",
            "X-Title": "AI File Robot",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    content = response.json()["choices"][0]["message"]["content"]
    return json.loads(content)
