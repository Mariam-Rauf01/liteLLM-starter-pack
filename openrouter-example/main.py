import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Tell me a joke."}]
}

response = requests.post(url, headers=headers, json=data)
print("Response:", response.json()["choices"][0]["message"]["content"])
