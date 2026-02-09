# MarketAI-Suite-Intelligent-Sales-and-Marketing-Development-Guide
MarketAI Suite uses Groq’s LLaMA 3.3 70B to streamline sales and marketing through three core data-driven features:  AI Campaign Generation: Automates marketing strategy.  Intelligent Pitch Creation: Tailors sales messaging.  Predictive Lead Scoring: Identifies high-value prospects.

# MarketAI Suite - AI-Powered Sales & Marketing Platform

MarketAI Suite is an intelligent assistant that combines advanced AI analysis with practical business intelligence to optimize sales and marketing operations . Powered by **Groq's LLaMA 3.3 70B model**, the platform delivers fast, actionable recommendations for campaign strategy and lead prioritization .

## 🚀 Key Features

*   **Campaign Generator:** Rapidly generates data-driven strategies, including 5 targeted content ideas and 3 ad copy variations .
*   **Sales Pitch Creator:** Crafts personalized 30-second elevator pitches, value propositions, and key differentiators .
*   **Intelligent Lead Scoring:** Quantifies lead quality on a 0–100 scale based on Budget, Need, Urgency, and Authority .
*   **Modern UI/UX:** A responsive dashboard featuring real-time processing feedback and formatted results .

## 🛠️ Technical Architecture

*   **Backend:** Flask (Python) .
*   **AI Engine:** Groq API (LLaMA 3.3 70B) .
*   **Frontend:** HTML5, CSS3 (Inter font), and JavaScript (Fetch API) .
*   **Tools:** Python Requests for API communication and Regular Expressions for text processing .

## 📋 Prerequisites

*   Python 3.8+
*   Groq API Key (from [Groq Console](https://console.groq.com))
*   Git 

## 🔧 Setup & Installation

1. **Clone the repo:** `git clone https://github.com/000-main/MarketAI-Suite-Intelligent-Sales-and-Marketing-Development-Guide.git`
2. **Install dependencies:** `pip install -r requirements.txt` 
3. **Configure API:** Create a `.env` file and add `GROQ_API_KEY=your_key_here` .
4. **Run Application:** `python app.py` .
5. **Access:** Navigate to `http://localhost:5000` .

## 📊 Lead Scoring Framework
*   **90-100:** Hot leads (immediate follow-up)
*   **75-89:** Warm leads (priority follow-up)
*   **60-74:** Lukewarm leads (nurture)
*   **Below 60:** Cold leads (defer/disqualify) 

---
*Developed as part of a SmartBridge SkillWallet project.*
