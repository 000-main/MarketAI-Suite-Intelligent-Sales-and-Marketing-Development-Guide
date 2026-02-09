import re
from typing import Dict, Optional

import streamlit as st
from groq import Groq


# ── CONFIGURATION & PROMPTS ──────────────────────────────────────────────
class Config:
    APP_NAME = "MarketAI Suite"
    APP_ICON = "📈"
    MODEL = "llama-3.3-70b-versatile"
    # Hardcoded key as per your requirement
    API_KEY = "Give_Your_Groq_api_key_here"

    PROMPTS = {
        "campaign": """Act as a Growth Architect. Create a GTM campaign for:
Product: {product} | Audience: {audience} | Platform: {platform}
Provide: 1. Objective, 2. Value Prop, 3. Pain Points, 4. 3 Creative Concepts, 5. Budget, 6. KPIs.""",
        "pitch": """Act as a Sales Consultant. Create a pitch for:
Product: {product} | Audience: {audience} | Context: {context}
Provide: 1. Hook, 2. Problem, 3. Solution, 4. Benefits, 5. Social Proof, 6. CTA.""",
        "scoring": """Develop a lead scoring framework for:
Product: {product} | Industry: {industry} | Cycle: {sales_cycle}
Provide: 1. Demographics, 2. Behaviors, 3. Engagement, 4. Intent Indicators, 5. Thresholds.""",
    }


# ── AI LOGIC ─────────────────────────────────────────────────────────────
def generate_ai_response(prompt_key: str, params: Dict[str, str]) -> Optional[str]:
    try:
        client = Groq(api_key=Config.API_KEY)
        prompt = Config.PROMPTS[prompt_key].format(**params)

        response = client.chat.completions.create(
            model=Config.MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Generation Error: {e}")
        return None


# ── UI STYLING ───────────────────────────────────────────────────────────
def inject_ui_style():
    st.markdown(
        """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Background and Layout */
    .stApp {
        background: #fdfdfd;
    }

    [data-testid="stSidebar"] {display: none;}
    [data-testid="stHeader"] {display: none;}
    .block-container {padding-top: 2rem;}

    /* Typography */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }

    .subtitle {
        color: #64748b;
        text-align: center;
        margin-bottom: 3rem;
        font-size: 1.1rem;
        font-weight: 500;
    }

    /* Dashboard Cards */
    .card {
        background: white;
        padding: 2.5rem 1.5rem;
        border-radius: 24px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        text-align: center;
        height: 220px;
        margin-bottom: 15px;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px -10px rgba(59, 130, 246, 0.15);
        border-color: #3b82f6;
    }

    .card h3 { font-size: 2.5rem; margin-bottom: 10px; }
    .card h4 { color: #1e293b; font-weight: 700; margin-bottom: 8px; }
    .card p { color: #64748b; font-size: 0.9rem; line-height: 1.4; }

    /* Forms and Inputs */
    .stTextInput input, .stSelectbox select {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        padding: 12px !important;
    }

    /* Result Container - FIXED GHOSTING/CURVE ERROR */
    .result-box {
        background: white;
        border-radius: 20px;
        padding: 30px;
        border: 1px solid #e2e8f0;
        border-left: 6px solid #3b82f6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-top: 25px;
        line-height: 1.6;
        color: #334155;
        min-height: 50px; /* Prevent collapse */
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        padding: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.02em;
        transition: all 0.2s ease;
    }

    .stButton>button[kind="primary"] {
        background: #3b82f6;
        border: none;
    }

    .back-btn button {
        width: auto !important;
        background: transparent !important;
        color: #64748b !important;
        border: 1px solid #e2e8f0 !important;
        margin-bottom: 2rem;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


# ── NAVIGATION LOGIC ─────────────────────────────────────────────────────
def navigate_to(page_name: str):
    st.session_state.page = page_name
    st.rerun()


# ── PAGES ────────────────────────────────────────────────────────────────
def render_dashboard():
    st.markdown('<h1 class="main-title">MarketAI Suite</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Next-generation Intelligence for High-Growth Teams</p>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="card"><h3>🚀</h3><h4>Campaigns</h4><p>Generate end-to-end GTM strategies & platform creative.</p></div>',
            unsafe_allow_html=True,
        )
        if st.button("Start Building", key="btn_camp"):
            navigate_to("campaign")

    with col2:
        st.markdown(
            '<div class="card"><h3>🎤</h3><h4>Sales Pitch</h4><p>Convert prospects with executive-level sales narratives.</p></div>',
            unsafe_allow_html=True,
        )
        if st.button("Draft Pitch", key="btn_pitch"):
            navigate_to("pitch")

    with col3:
        st.markdown(
            '<div class="card"><h3>⭐</h3><h4>Lead Scoring</h4><p>Identify high-intent buyers with AI qualification frameworks.</p></div>',
            unsafe_allow_html=True,
        )
        if st.button("Optimize Scoring", key="btn_score"):
            navigate_to("scoring")


def render_tool_header(title, icon):
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard"):
        navigate_to("home")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(f"## {icon} {title}")
    st.markdown("---")


def render_campaign():
    render_tool_header("Campaign Generator", "🚀")

    col1, col2 = st.columns(2)
    product = col1.text_input("Product/Service Name", placeholder="e.g. Nexus CRM")
    audience = col2.text_input(
        "Ideal Customer Persona", placeholder="e.g. VPs of Sales in Fintech"
    )
    platform = st.selectbox(
        "Primary Channel",
        ["LinkedIn Ads", "Google Search", "Meta Ads", "Cold Email Outbound"],
    )

    if st.button("Generate Strategy", type="primary"):
        if product and audience:
            with st.spinner("Analyzing market dynamics..."):
                res = generate_ai_response(
                    "campaign",
                    {"product": product, "audience": audience, "platform": platform},
                )
                if res:
                    # Wrapped in a single markdown block to prevent UI glitch
                    st.markdown(
                        f'<div class="result-box">{res}</div>', unsafe_allow_html=True
                    )
                    st.download_button(
                        "Export as Markdown", res, file_name=f"{product}_campaign.md"
                    )
        else:
            st.error("Missing required fields.")


def render_pitch():
    render_tool_header("Sales Pitch Craft", "🎤")

    col1, col2 = st.columns(2)
    product = col1.text_input("What are you selling?")
    audience = col2.text_input("Who is the decision maker?")
    context = st.selectbox(
        "Conversation Stage",
        ["Cold Outreach", "Discovery Call", "Final Executive Pitch", "Renewal Brief"],
    )

    if st.button("Generate Pitch", type="primary"):
        if product and audience:
            with st.spinner("Drafting high-conversion pitch..."):
                res = generate_ai_response(
                    "pitch",
                    {"product": product, "audience": audience, "context": context},
                )
                if res:
                    st.markdown(
                        f'<div class="result-box">{res}</div>', unsafe_allow_html=True
                    )
                    st.download_button(
                        "Export as Markdown", res, file_name="pitch_script.md"
                    )


def render_scoring():
    render_tool_header("Lead Scoring Framework", "⭐")

    col1, col2 = st.columns(2)
    product = col1.text_input("Product Name")
    industry = col2.text_input("Target Industry Vertical")
    cycle = st.selectbox(
        "Sales Complexity",
        ["Transactional (Fast)", "Medium Market", "Enterprise (High-Touch)"],
    )

    if st.button("Build Framework", type="primary"):
        if product and industry:
            with st.spinner("Constructing scoring matrix..."):
                res = generate_ai_response(
                    "scoring",
                    {"product": product, "industry": industry, "sales_cycle": cycle},
                )
                if res:
                    st.markdown(
                        f'<div class="result-box">{res}</div>', unsafe_allow_html=True
                    )
                    st.download_button(
                        "Export as Markdown", res, file_name="lead_scoring.md"
                    )


# ── MAIN APP ENTRY ───────────────────────────────────────────────────────
def main():
    st.set_page_config(
        page_title="MarketAI Suite",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_ui_style()

    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Routing logic
    if st.session_state.page == "home":
        render_dashboard()
    elif st.session_state.page == "campaign":
        render_campaign()
    elif st.session_state.page == "pitch":
        render_pitch()
    elif st.session_state.page == "scoring":
        render_scoring()


if __name__ == "__main__":
    main()
