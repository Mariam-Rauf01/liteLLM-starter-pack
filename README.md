# 🧠 LLM Starter Pack

This repository showcases three minimal and clear Python projects to help you get started with:

* ⚡ [**UV**](https://github.com/astral-sh/uv) — Ultra-fast Python package manager
* 🌐 [**OpenRouter**](https://openrouter.ai/) — Unified API for multiple LLMs
* 🤖 [**LiteLLM**](https://github.com/BerriAI/litellm) — Drop-in LLM interface for OpenAI, OpenRouter, and more

---

## 📁 Project Structure

```
llm-starter-pack/
├── uv-example/            # Fetch a joke via API using UV
├── openrouter-example/    # Get LLM response via OpenRouter
├── litellm-example/       # Use LiteLLM to call OpenRouter/OpenAI
```

---

## 🚀 Quick Start Guide

Each folder is self-contained with its own `main.py` and `requirements.txt`.

### 🔹 1. UV Example

**📁 `uv-example/main.py`**

* Fetches a joke using a public API

```bash
cd uv-example
uv venv
uv pip install -r requirements.txt
uv run python main.py
```

---

### 🔹 2. OpenRouter Example

**📁 `openrouter-example/main.py`**

* Calls GPT-3.5 via OpenRouter

#### 🛠 Setup

Create a `.env` file:

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
```

Run it:

```bash
cd openrouter-example
uv pip install -r requirements.txt
uv run python main.py
```

---

### 🔹 3. LiteLLM Example

**📁 `litellm-example/main.py`**

* Unified wrapper to call OpenRouter or OpenAI

#### 🛠 Setup

Create a `.env` file:

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxx
# or
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

Run it:

```bash
cd litellm-example
uv pip install -r requirements.txt
uv run python main.py
```

---

## ✅ Example Output

```
Did you know? Octopuses have three hearts!
```

---

## 📌 Requirements

* Python 3.10+
* `uv` installed globally:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

## 📜 License

MIT License

---

## 🙌 Author

**Mariam Rauf** — Learning, building, and sharing AI tools with Python 🚀



