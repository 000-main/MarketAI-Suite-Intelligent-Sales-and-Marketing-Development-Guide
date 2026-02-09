# MarketAI-Suite-Intelligent-Sales-and-Marketing-Development-Guide
MarketAI Suite uses Groq’s LLaMA 3.3 70B to streamline sales and marketing through three core data-driven features:  AI Campaign Generation: Automates marketing strategy.  Intelligent Pitch Creation: Tailors sales messaging.  Predictive Lead Scoring: Identifies high-value prospects.

# MarketAI Suite - AI-Powered Sales & Marketing Platform

MarketAI Suite is an intelligent assistant that combines advanced AI analysis with practical business intelligence to optimize sales and marketing operations [1, 9]. Powered by **Groq's LLaMA 3.3 70B model**, the platform delivers fast, actionable recommendations for campaign strategy and lead prioritization [1].

## 🚀 Key Features

*   **Campaign Generator:** Rapidly generates data-driven strategies, including 5 targeted content ideas and 3 ad copy variations [2, 3].
*   **Sales Pitch Creator:** Crafts personalized 30-second elevator pitches, value propositions, and key differentiators [4].
*   **Intelligent Lead Scoring:** Quantifies lead quality on a 0–100 scale based on Budget, Need, Urgency, and Authority [5, 6].
*   **Modern UI/UX:** A responsive dashboard featuring real-time processing feedback and formatted results [8, 10].

## 🛠️ Technical Architecture

*   **Backend:** Flask (Python) [7].
*   **AI Engine:** Groq API (LLaMA 3.3 70B) [7, 11].
*   **Frontend:** HTML5, CSS3 (Inter font), and JavaScript (Fetch API) [7, 12].
*   **Tools:** Python Requests for API communication and Regular Expressions for text processing [7].

## 📋 Prerequisites

*   Python 3.8+
*   Groq API Key (from [Groq Console](https://console.groq.com))
*   Git [13]

## 🔧 Setup & Installation

1. **Clone the repo:** `git clone <your-repo-url>`
2. **Install dependencies:** `pip install -r requirements.txt` [14]
3. **Configure API:** Create a `.env` file and add `GROQ_API_KEY=your_key_here` [14].
4. **Run Application:** `python app.py` [12].
5. **Access:** Navigate to `http://localhost:5000` [12].

## 📊 Lead Scoring Framework
*   **90-100:** Hot leads (immediate follow-up)
*   **75-89:** Warm leads (priority follow-up)
*   **60-74:** Lukewarm leads (nurture)
*   **Below 60:** Cold leads (defer/disqualify) [6]

---
*Developed as part of a SmartBridge SkillWallet project.*
