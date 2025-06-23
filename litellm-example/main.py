# 3. LiteLLM Example

# What is LiteLLM?

# An unified interface to call LLMs (OpenAI, Claude, Mistral, etc.) using a simple Python API or hosted proxy.

import os
from dotenv import load_dotenv
import litellm

load_dotenv()

litellm.api_base = "https://openrouter.ai/api/v1"
litellm.api_key = os.getenv("OPENROUTER_API_KEY")

response = litellm.completion(
    model="openrouter/openai/gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me a fun fact."}]
)

print(response['choices'][0]['message']['content'])