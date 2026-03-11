"""Flask server for Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main webpage."""
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze emotion from user input text."""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    return str(response)


app.run(host="0.0.0.0", port=5000)
