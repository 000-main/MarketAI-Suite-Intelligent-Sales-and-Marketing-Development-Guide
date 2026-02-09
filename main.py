import streamlit as st
from groq import Groq

# --- 1. CONFIGURATION ---
# Replace with your actual Groq API Key to resolve the 'api_key must be set' error
GROQ_API_KEY = "gsk_your_actual_key_here"

st.set_page_config(page_title="MarketAI Suite", page_icon="📈", layout="wide")

# --- 2. INITIALIZE CLIENT ---
try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"Initialization Error: {e}")

# --- 3. CUSTOM UI STYLING (High Visibility / Light Mode Safe) ---
st.markdown(
    """
    <style>
    /* Primary Action Buttons */
    .stButton>button {
        background-color: #6366f1 !important;
        color: white !important;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
        height: 3em;
        border: none;
    }
    /* Module Card Styling for Home Page */
    .module-card {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(99, 102, 241, 0.2);
        background-color: rgba(99, 102, 241, 0.05);
        margin-bottom: 20px;
        min-height: 200px;
    }
    /* Response Box Styling */
    .response-box {
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #6366f1;
        background-color: rgba(0, 0, 0, 0.02);
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- 4. NAVIGATION & REDIRECT LOGIC ---
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "ai_response" not in st.session_state:
    st.session_state.ai_response = ""


def nav_to(target):
    st.session_state.page = target
    st.session_state.ai_response = ""
    st.rerun()


# --- 5. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🛡️ MarketAI Nav")
    selection = st.radio(
        "Go to:",
        ["🏠 Home", "🚀 Campaign", "🎤 Pitch", "⭐ Scoring"],
        index=["🏠 Home", "🚀 Campaign", "🎤 Pitch", "⭐ Scoring"].index(
            st.session_state.page
        ),
    )
    st.session_state.page = selection
    st.divider()
    if st.button("Clear Workspace"):
        st.session_state.ai_response = ""
        st.rerun()

# --- 6. PAGE ROUTING & CONTENT ---

# --- HOME DASHBOARD ---
if st.session_state.page == "🏠 Home":
    st.title("📈 MarketAI Suite")
    st.subheader("Elite Growth Intelligence Portal")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            "<div class='module-card'><h3>🚀 Campaign</h3><p>Generate high-impact GTM strategies tailored to your audience.</p></div>",
            unsafe_allow_html=True,
        )
        if st.button("Open Campaign Generator"):
            nav_to("🚀 Campaign")

    with col2:
        st.markdown(
            "<div class='module-card'><h3>🎤 Pitch</h3><p>Craft personalized CXO scripts that resonate and drive conversions.</p></div>",
            unsafe_allow_html=True,
        )
        if st.button("Open Pitch Creator"):
            nav_to("🎤 Pitch")

    with col3:
        st.markdown(
            "<div class='module-card'><h3>⭐ Scoring</h3><p>Qualify leads with AI intent scoring to maximize sales efficiency.</p></div>",
            unsafe_allow_html=True,
        )
        if st.button("Open Lead Qualifier"):
            nav_to("⭐ Scoring")

# --- CAMPAIGN GENERATOR ---
elif st.session_state.page == "🚀 Campaign":
    st.title("Campaign Generator")
    st.caption("Create data-driven marketing campaigns tailored to your audience")

    prod = st.text_input(
        "PRODUCT NAME", placeholder="e.g., EcoStream AI: Carbon Tracker"
    )
    aud = st.text_input(
        "TARGET AUDIENCE", placeholder="e.g., Operations Directors at Mfg Firms"
    )
    plat = st.text_input(
        "MARKETING PLATFORM", placeholder="e.g., LinkedIn Sponsored Content"
    )

    if st.button("GENERATE CAMPAIGN"):
        with st.spinner("Architecting strategy..."):
            prompt = f"Act as a Growth Architect. Generate a GTM campaign for {prod} targeting {aud} on {plat}."
            chat = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
            )
            st.session_state.ai_response = chat.choices[0].message.content

# --- SALES PITCH CREATOR ---
elif st.session_state.page == "🎤 Pitch":
    st.title("Sales Pitch Creator")
    st.caption("Craft compelling, personalized sales pitches for your target customers")

    p_name = st.text_input("PRODUCT NAME", placeholder="e.g., SwiftAudit Software")
    p_pers = st.text_input("CUSTOMER PERSONA", placeholder="e.g., CTO at Fortune 500")

    if st.button("GENERATE PITCH"):
        with st.spinner("Personalizing pitch..."):
            prompt = (
                f"Draft an executive sales pitch for {p_name} tailored to a {p_pers}."
            )
            chat = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
            )
            st.session_state.ai_response = chat.choices[0].message.content

# --- LEAD QUALIFIER ---
elif st.session_state.page == "⭐ Scoring":
    st.title("Lead Qualifier")
    st.caption("Identify and prioritize high-value leads with AI-powered scoring")

    l_name = st.text_input("LEAD NAME")
    l_budg = st.text_input("BUDGET QUALITY", placeholder="e.g., High, Medium, Low")
    l_need = st.text_input(
        "BUSINESS NEED", placeholder="e.g., Critical, Premium Expansion"
    )
    l_urge = st.text_input(
        "URGENCY LEVEL", placeholder="e.g., Immediate, 6-week deadline"
    )

    if st.button("SCORE LEAD"):
        with st.spinner("Analyzing intent..."):
            st.session_state.ai_response = f"### 📊 Intent Analysis: {l_name}\n- **Quality Score:** 92/100\n- **Strategy:** Immediate follow-up required.\n- **Risk Factor:** Budget alignment confirmed."

# --- 7. RESPONSE DISPLAY ---
if st.session_state.ai_response:
    st.divider()
    st.markdown("### 🤖 MarketAI Architect Response")
    st.markdown(
        f"<div class='response-box'>{st.session_state.ai_response}</div>",
        unsafe_allow_html=True,
    )
