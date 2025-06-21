# 💬 Chat with Any Website Content · Streamlit Chatbot

Ask questions about **any website** and get answers that are **strictly** grounded in that site’s own pages.

| Feature | What it does |
|---------|--------------|
| 🌐 **Domain-scoped search** | Tavily fetches only pages from the base URL you give. |
| 🤖 **Gemini 2.5 Flash** | Generates concise, well-structured Markdown answers. |
| 🖥️ **Two-column UI** | Left: URL + question.  Right: scrollable answer box. |
| 🔒 **No hallucinations** | Prompt forbids any knowledge beyond the retrieved passages. |

---

## 📺 Demo

[![Watch the demo](https://img.youtube.com/vi/TrLWcVnaKB8/0.jpg)](https://youtu.be/TrLWcVnaKB8?si=1JduS9oH_X5MdqxZ)

*(Click the thumbnail to view on YouTube.)*

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone <your-repo-url>
cd <repo-dir>

# 2. Install
pip install -r requirements.txt

# 3. API keys
export TAVILY_API_KEY="sk-..."
export GOOGLE_API_KEY="AIza..."

# 4. Run
streamlit run app.py


⸻

🖥️ How to Use
	1.	Base URL – enter only the root domain (e.g. https://occamsadvisory.com).
	2.	Question – type what you want to know.
	3.	Click Answer.
	4.	Read the right-hand box:
	•	Bold one-sentence summary
	•	Bold section headings
	•	Concise bullet/numbered lists
	•	Scroll if the answer is long.

Tip: If you paste a URL with a path or query string, the app asks you to correct it.

⸻

🗂️ Project Files

File	Purpose
app.py	Streamlit UI + LangChain logic
requirements.txt	Python dependencies
README.md	Project overview (this file)


⸻

⚙️ Environment Variables

Variable	Description	Where to get it
TAVILY_API_KEY	Tavily search API key	https://app.tavily.com/
GOOGLE_API_KEY	Google Generative AI key	https://makersuite.google.com/

You can also put these in a .env file; the app will read them automatically.

⸻

📦 Built With
	•	Streamlit – rapid web UI
	•	LangChain – agent orchestration
	•	Gemini 2.5 Flash – LLM via langchain-google-genai
	•	Tavily – quick, domain-restricted search
	•	python-dotenv – easy env-var management

⸻

📝 License

MIT — see LICENSE for details.
Feel free to fork, remix, and improve!

