from functools import wraps

from flask import Flask, Response, jsonify, render_template, request
from flask_cloudflared import run_with_cloudflared  # The "Magic" Library
from groq import Groq

app = Flask(__name__)
run_with_cloudflared(app)  # This opens the tunnel to the internet

# --- CONFIGURATION & SECURITY ---
API_KEY = "Groq_api_key_here"
MODEL = "llama-3.3-70b-versatile"

# SET YOUR CREDENTIALS HERE
USER_ID = "admin"
USER_PASS = "marketai2024"

client = Groq(api_key=API_KEY)


# --- AUTHENTICATION LOGIC ---
def check_auth(username, password):
    return username == USER_ID and password == USER_PASS


def authenticate():
    return Response(
        "Login Required to access MarketAI Suite.",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


# --- ROUTES ---


@app.route("/")
@requires_auth
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
@requires_auth
def generate():
    data = request.json
    tool = data.get("tool")
    params = data.get("params")

    prompts = {
        "campaign": "Act as a Growth Architect. GTM campaign for: Product: {product} | Audience: {audience} | Platform: {platform}.",
        "pitch": "Act as a Sales Consultant. Pitch for: Product: {product} | Audience: {audience} | Context: {context}.",
        "scoring": "Lead scoring framework for: Product: {product} | Industry: {industry} | Cycle: {sales_cycle}.",
    }

    try:
        if tool == "master":
            prompt = f"Act as a world-class {params.get('role')}. Answer: {params.get('query')}"
        else:
            prompt = prompts[tool].format(**params)

        res = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}], model=MODEL, temperature=0.7
        )
        return jsonify({"success": True, "result": res.choices[0].message.content})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    # When you run this, look at the terminal for the "trycloudflare.com" link
    app.run()
