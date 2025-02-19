from flask import Flask, request, jsonify
from flask_cors import CORS
from better_profanity import profanity

app = Flask(__name__)
CORS(app)  # Allow frontend requests

profanity.load_censor_words()
profanity.add_censor_words(["stupid", "dumb", "loser", "idiot", "moron", "trash"])

@app.route("/check-comment", methods=["POST"])
def check_comment():
    try:
        print("🔹 Received Request:", request.data)  # Debug raw data
        data = request.get_json()

        if not data or "text" not in data:
            print("❌ ERROR: Invalid JSON received!")
            return jsonify({"error": "Invalid JSON"}), 400

        text = data.get("text", "").strip()
        print(f"📩 Comment Received: {text}")  # Debug log

        contains_profanity = profanity.contains_profanity(text)
        print(f"🔍 Contains Profanity? {contains_profanity}")  # Debug log

        if contains_profanity:
            return jsonify({"allowed": False, "message": "Offensive content detected!"})
        
        return jsonify({"allowed": True, "message": "Content is clean."})

    except Exception as e:
        print(f"🔥 ERROR: {e}")
        return jsonify({"error": "Server error"}), 500

if __name__ == "__main__":
    print("🚀 Flask Server Running on http://localhost:5000/")
    app.run(debug=True, port=5000)

