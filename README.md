# 🧠 LLM Starter Pack

This repository contains three simple and well-organized examples to help you get started with:

- 🧰 [**UV**](https://github.com/astral-sh/uv) — Fast Python package & environment manager
- 🌐 [**OpenRouter**](https://openrouter.ai/) — Unified API for multiple LLM providers
- 🤖 [**LiteLLM**](https://github.com/BerriAI/litellm) — Simplified wrapper for calling LLMs

---

## 📁 Project Structure

llm-starter-pack/
├── uv-example/ # Uses UV to fetch a joke from a public API
├── openrouter-example/ # Uses OpenRouter to get an LLM response
├── litellm-example/ # Uses LiteLLM to call an LLM (OpenAI or OpenRouter)

yaml
Copy
Edit


---

## 🚀 Quick Start

Each example folder contains its own code, dependencies, and instructions.

---

### 🔹 1. UV Example

#### 📁 `uv-example/main.py`

Uses `uv` to run a Python script that fetches a random joke.

#### 🛠 Setup

```bash
cd uv-example
uv venv
uv pip install -r requirements.txt
uv run python main.py

🔹 2. OpenRouter Example
📁 openrouter-example/main.py
Calls GPT-3.5 via OpenRouter API.

🛠 Setup
Copy .env.example to .env and add your OpenRouter API key:

env
Copy
Edit
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
Then run:

bash
Copy
Edit
cd openrouter-example
uv pip install -r requirements.txt
uv run python main.py
🔹 3. LiteLLM Example
📁 litellm-example/main.py
Uses LiteLLM to access OpenRouter (or OpenAI) via a unified interface.

🛠 Setup
Copy .env.example to .env and add your OpenRouter or OpenAI API key:

env
Copy
Edit
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
# or
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
Run the example:

bash
Copy
Edit
cd litellm-example
uv pip install -r requirements.txt
uv run python main.py
✅ Output Example
Each script will print a response from an LLM or a joke API.

Example output:

nginx
Copy
Edit
Did you know? Octopuses have three hearts!
📌 Requirements
Python 3.10+

uv installed globally:

bash
Copy
Edit
curl -Ls https://astral.sh/uv/install.sh | sh
📄 License
This project is open-source and free to use under the MIT License.

yaml
Copy
Edit

---

Would you like me to generate the `.md` file and include it in a `.zip` or GitHub push-ready repo?








