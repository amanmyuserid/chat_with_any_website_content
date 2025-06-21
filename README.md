# 💬 Chat with Any Website Content · Streamlit Chatbot

A two-column Streamlit app that lets you ask questions about **any website** and receive answers grounded **only** in that site’s content.  
Under the hood it:

1. Accepts a *base URL* and a *question* from the user.  
2. Runs a domain-restricted Tavily search to fetch relevant pages.  
3. Uses Google Gemini (via LangChain) plus the retrieved passages to generate a concise, well-formatted Markdown answer.  
4. Displays the reply inside a boxed, scrollable area so long outputs never break the layout.

---

## ✨ Demo



---

## 🚀 Quick start

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd <repo-dir>

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API keys (Tavily & Google)
export TAVILY_API_KEY="sk-..."
export GOOGLE_API_KEY="AIza..."

# 4. Launch the app
streamlit run app.py


⸻

🗂️ Project files

File	Purpose
app.py	Streamlit UI + LangChain logic
requirements.txt	Python package list
README.md	You’re reading it


⸻

⚙️ Environment variables

Key	Description	Where to get it
TAVILY_API_KEY	Auth token for Tavily search API	https://app.tavily.com/
GOOGLE_API_KEY	Google Generative AI key (for Gemini)	https://makersuite.google.com/

You can set them in a .env file, your shell profile, or Streamlit’s sidebar prompts.

⸻

🖥️ Usage
	1.	Base URL – enter only the domain root (e.g. https://occamsadvisory.com).
	2.	Question – type what you want to know.
	3.	Click Answer.
	4.	The right-hand box shows a one-sentence summary followed by structured bullet points.

Tips:
	•	If you provide a URL with a path/query, the app will ask you to correct it.
	•	Long answers are scrollable inside the box.
	•	The LLM is instructed not to use any info beyond what Tavily returned.

⸻

📦 Built with
	•	Streamlit – rapid web UI
	•	LangChain – agent & prompt orchestration
	•	Gemini 2.5 Flash – LLM via langchain-google-genai
	•	Tavily – fast, domain-scoped web search
	•	python-dotenv – .env support

⸻

📝 License

MIT — see LICENSE for details.
Feel free to fork, remix, and improve!

