from flask import Flask, jsonify, render_template, request
from groq import Groq

app = Flask(__name__)

# CONFIGURATION
API_KEY = "Groq_api_key_here"

MODEL = "llama-3.3-70b-versatile"
client = Groq(api_key=API_KEY)

PROMPTS = {
    "campaign": "Act as a Growth Architect. Create a GTM campaign for: Product: {product} | Audience: {audience} | Platform: {platform}.",
    "pitch": "Act as a Sales Consultant. Create a pitch for: Product: {product} | Audience: {audience} | Context: {context}.",
    "scoring": "Develop a lead scoring framework for: Product: {product} | Industry: {industry} | Cycle: {sales_cycle}.",
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    tool = data.get("tool")
    params = data.get("params")

    try:
        if tool == "master":
            # Dynamic Master Prompt Logic
            role = params.get("role", "Expert Consultant")
            query = params.get("query", "")
            prompt = f"Act as a world-class {role}. Answer the following query with high-level professional insight: {query}"
        else:
            prompt = PROMPTS[tool].format(**params)

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL,
            temperature=0.7,
        )
        return jsonify(
            {"success": True, "result": chat_completion.choices[0].message.content}
        )
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
