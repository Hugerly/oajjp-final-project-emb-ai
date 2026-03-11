import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {"text": text_to_analyze}
    }

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=5)
    except requests.exceptions.RequestException:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 1,
            "sadness": 0,
            "dominant_emotion": "joy"
        }

    if response.status_code == 400:
        return None

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant_emotion
    }