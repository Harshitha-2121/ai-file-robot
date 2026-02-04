import requests

API_KEY = "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"

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI File Robot Test",
        "Content-Type": "application/json"
    },
    json={
        "model": "google/gemini-flash-1.5",
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    }
)

print(response.status_code)
print(response.json())
