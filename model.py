# model.py
from transformers import pipeline

# Load the pre-trained emotion detection model
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")


def predict_emotion(text):
    """
    Predict the emotion in the given text using a pre-trained model.
    """
    result = emotion_model(text)
    emotion = result[0]['label']
    return emotion
