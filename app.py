from flask import Flask, render_template, request, jsonify, session
from groq import Groq
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.secret_key = "supersecretkey"  # needed for session

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize chat memory
def init_chat():
    if "messages" not in session:
        session["messages"] = [
            {"role": "system", "content": "You are a helpful AI assistant like ChatGPT."}
        ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")

    init_chat()

    # Add user message to history
    session["messages"].append({"role": "user", "content": user_msg})

    # Send to Groq
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=session["messages"]
    )

    bot_reply = completion.choices[0].message.content

    # Save bot response
    session["messages"].append({"role": "assistant", "content": bot_reply})

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)