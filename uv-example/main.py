# 1. UV Example (Python Environment & Package Management)

# What is UV?

# A fast Python package manager and virtual environment tool by Astral.

import requests

print("Fetching a joke...")
response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
print("Joke:", response.json().get("joke"))
