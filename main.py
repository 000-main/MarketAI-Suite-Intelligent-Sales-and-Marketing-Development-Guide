import os

import streamlit as st
from groq import Groq

st.set_page_config(page_title="MarketAI Suite Portal", page_icon="📈", layout="wide")

# --- AUTHENTICATION CONFIGURATION ---
PORTAL_PASSWORD = "pass"  # Change this to your preferred password
GROQ_KEY = "your_groq_api_key"  # Insert your API key here

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


def login_screen():
    st.title("🛡️ MarketAI Suite Access")
    pwd = st.text_input("Enter Architect Credentials", type="password")
    if st.button("Unlock Portal"):
        if pwd == PORTAL_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Unauthorized Access: Invalid Credentials")


if not st.session_state.authenticated:
    login_screen()
    st.stop()

# --- PORTAL INITIALIZATION ---
client = Groq(api_key=GROQ_KEY)

st.title("🛡️ MarketAI Suite: Strategic Growth Architect")
st.markdown("### Elite B2B/B2C Growth Intelligence")
st.divider()

with st.sidebar:
    st.header("Campaign Settings")
    model = st.selectbox(
        "Intelligence Model", ["llama-3.3-70b-versatile", "llama-3-8b-8192"]
    )
    temp = st.slider("Strategy Creative Variance", 0.0, 1.0, 0.7)
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

SYSTEM_PROMPT = (
    "Act as the MarketAI Suite Strategic Growth Architect, an elite consultant with 20+ years of experience. "
    "Mission: Provide high-impact, executive-level guidance on lead identification and multi-channel outreach. "
    "Format: Use tables for data, bold key terms, and always conclude with a 'Next Action Step' or 'Pro-Tip'."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your growth challenge..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages,
            ],
            temperature=temp,
            stream=True,
        )

        for chunk in completion:
            content = chunk.choices[0].delta.content or ""
            full_response += content
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
