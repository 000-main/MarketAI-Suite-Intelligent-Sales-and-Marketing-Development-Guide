import streamlit as st
from groq import Groq

# --- CONFIGURATION ---
# Replace with your actual Groq API Key
GROQ_API_KEY = "gsk_your_key_here"

st.set_page_config(page_title="MarketAI Suite", page_icon="📈", layout="wide")

# --- INITIALIZE CLIENT ---
# This line fixes the GroqError by explicitly passing the key
try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"Configuration Error: {e}")
    st.stop()

# --- SYSTEM PROMPT ---
ARCHITECT_PROMPT = (
    "Act as the MarketAI Suite Strategic Growth Architect. Provide high-impact, "
    "executive-level guidance. Use tables for data, bold key terms, and "
    "conclude with a 'Next Action Step' or 'Pro-Tip'."
)

# --- UI NAVIGATION ---
st.title("📈 MarketAI Suite")
tabs = st.tabs(["Home", "Campaign", "Pitch", "Lead Score"])

# --- HOME TAB ---
with tabs[0]:
    st.markdown("### Welcome to the Growth Intelligence Hub")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Campaign Generator**: Data-driven strategies.")
    with col2:
        st.info("**Sales Pitch Creator**: Compelling personalization.")
    with col3:
        st.info("**Lead Qualifier**: Intelligent scoring.")

# --- CAMPAIGN GENERATOR ---
with tabs[1]:
    st.subheader("Campaign Generator")
    st.caption("Create data-driven marketing campaigns tailored to your audience")
    c_prod = st.text_input(
        "PRODUCT NAME", placeholder="e.g., AI Analytics Platform", key="c_prod"
    )
    c_aud = st.text_input(
        "TARGET AUDIENCE", placeholder="e.g., Health-conscious millennials", key="c_aud"
    )
    c_plat = st.text_input(
        "MARKETING PLATFORM",
        placeholder="e.g., LinkedIn, Instagram, Twitter, Email",
        key="c_plat",
    )

    if st.button("GENERATE CAMPAIGN", type="primary"):
        with st.spinner("Architecting..."):
            prompt = f"Create a campaign for {c_prod} targeting {c_aud} on {c_plat}."
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": ARCHITECT_PROMPT},
                    {"role": "user", "content": prompt},
                ],
            )
            st.markdown(response.choices[0].message.content)

# --- SALES PITCH CREATOR ---
with tabs[2]:
    st.subheader("Sales Pitch Creator")
    st.caption("Craft compelling, personalized sales pitches for your target customers")
    p_prod = st.text_input(
        "PRODUCT NAME",
        placeholder="e.g., Dairy Milk Silk Premium Chocolate",
        key="p_prod",
    )
    p_persona = st.text_input(
        "CUSTOMER PERSONA",
        placeholder="e.g., CTO at Fortune 500, Retail Manager",
        key="p_persona",
    )

    if st.button("GENERATE PITCH", type="primary"):
        with st.spinner("Crafting..."):
            prompt = f"Craft a sales pitch for {p_prod} tailored to a {p_persona}."
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": ARCHITECT_PROMPT},
                    {"role": "user", "content": prompt},
                ],
            )
            st.markdown(response.choices[0].message.content)

# --- LEAD QUALIFIER ---
with tabs[3]:
    st.subheader("Lead Qualifier")
    st.caption("Identify and prioritize high-value leads with AI-powered scoring")
    l_name = st.text_input("LEAD NAME", placeholder="e.g., Rajesh Kumar, John Smith")
    l_budget = st.text_input(
        "BUDGET QUALITY", placeholder="e.g., High, Medium, Low, 50 lakhs"
    )
    l_need = st.text_input(
        "BUSINESS NEED", placeholder="e.g., Critical, Important, Premium Expansion"
    )
    l_urgency = st.text_input(
        "URGENCY LEVEL", placeholder="e.g., Immediate, Short-term, 6-week deadline"
    )

    if st.button("SCORE LEAD", type="primary"):
        with st.spinner("Analyzing intent..."):
            prompt = f"Score this lead: Name: {l_name}, Budget: {l_budget}, Need: {l_need}, Urgency: {l_urgency}."
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": ARCHITECT_PROMPT},
                    {"role": "user", "content": prompt},
                ],
            )
            st.markdown(response.choices[0].message.content)
