# Chat with any website content – Two‑Column Chatbot (v9: boxed, scrollable answer)
# =====================================================================
# Updates
# -------
# • Answer section is now wrapped in a bordered rectangle (same visual style
#   as inputs). If the content exceeds the box height, a vertical scrollbar
#   appears so the layout stays within a single screen.
# • Title remains centred; all other behaviour is unchanged.

import os
import streamlit as st
from urllib.parse import urlparse
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

# ---------------------------------------------------------------------------
# 1. Page setup & environment
# ---------------------------------------------------------------------------
load_dotenv()
st.set_page_config(page_title="Chat with any website content", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🔎 Chat with any website content</h1>",
    unsafe_allow_html=True,
)

# Sidebar for API keys (only shows if missing) --------------------------------
if not os.getenv("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = st.sidebar.text_input("Tavily API Key", type="password")
if not os.getenv("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = st.sidebar.text_input("Google API Key", type="password")

if not (os.getenv("TAVILY_API_KEY") and os.getenv("GOOGLE_API_KEY")):
    st.info("Enter both API keys to continue.")
    st.stop()

# ---------------------------------------------------------------------------
# 2. Custom CSS – adds .box style with scroll for answer
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .box {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1rem;
            background: #ffffff;
        }
        /* answer specific: limit height & scroll */
        #answer-box.box {
            max-height: 450px;
            overflow-y: auto;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# 3. UI layout – two columns
# ---------------------------------------------------------------------------
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.subheader("Website & Query")
    base_url_input = st.text_input("Base URL", placeholder="https://www.amazon.in")
    query_input = st.text_area("Question", height=180, placeholder="What are the contact details or what is the price of macbook air m4 256gb?")
    run = st.button("Answer", key="answer_btn")

with right_col:
    st.subheader("Answer")
    # placeholder for boxed answer
    answer_placeholder = st.empty()

# ---------------------------------------------------------------------------
# 4. Helper – base URL validation
# ---------------------------------------------------------------------------

def validate_base_url(url: str):
    p = urlparse(url if url.startswith("http") else "https://" + url)
    if not p.netloc:
        return None, "URL missing domain."
    if p.path not in ("", "/") or p.query or p.params or p.fragment:
        return None, "Provide only the base URL (no extra path/query)."
    return p.netloc, None

# ---------------------------------------------------------------------------
# 5. Main interaction
# ---------------------------------------------------------------------------
if run:
    base_url = base_url_input.strip()
    query = query_input.strip()

    if not base_url or not query:
        st.warning("Both base URL and query are required.")
        st.stop()

    domain, err = validate_base_url(base_url)
    if err:
        st.error(err)
        st.stop()

    # Dynamic LLM / search tool for the domain --------------------------------
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20", temperature=0)

    tavily_tool = TavilySearchResults(
        max_results=5,
        include_answer=True,
        include_raw_content=True,
        include_domains=[domain],
    )

    system_msg = (
        f"You are a helpful assistant. **Strictly** answer **only** with information found in passages retrieved via the Tavily search from {domain}."
        f"Do **not** use prior knowledge, external facts, or assumptions."
        f"Begin with a brief answer sentence, then provide key "
        f"details(mention all the details, donot miss even any small information according to the query) as bulleted or numbered Markdown lists. Leave a blank line "
        f"between separate topics for readability. Avoid long paragraphs."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    agent = create_tool_calling_agent(llm, [tavily_tool], prompt)
    agent_exec = AgentExecutor(agent=agent, tools=[tavily_tool], verbose=False)

    # Generate answer ---------------------------------------------------------
    with st.spinner("Generating answer …"):
        try:
            resp = agent_exec.invoke({"input": query})
            ans = resp.get("output", "(No answer returned)")
        except Exception as e:
            ans = f"Error: {e}"

    # Render within a scrollable box -----------------------------------------
    answer_placeholder.markdown(
        f"<div id='answer-box' class='box'>{ans}</div>", unsafe_allow_html=True
    )
