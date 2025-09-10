from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import predict_emotion

app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route("/")
def home():
    return render_template("index.html")  # Frontend page


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if user_message:
        emotion = predict_emotion(user_message)
        response = f"Emotion Detected: {emotion}. Would you like to talk more about it?"
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'No message provided!'}), 400


if __name__ == "__main__":
    app.run(debug=True)
