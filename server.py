"""Flask server for emotion detection application."""

from flask import Flask, request, jsonify
from emotion import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Analyze emotion and handle errors."""
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    return jsonify(result)


@app.route("/")
def home():
    """Home route."""
    return "Emotion Detection API is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
