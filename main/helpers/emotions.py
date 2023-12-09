from transformers import pipeline, RobertaTokenizer, RobertaForSequenceClassification


model_name = "SamLowe/roberta-base-go_emotions"
classifier = pipeline(
    task="text-classification",
    model=RobertaForSequenceClassification.from_pretrained(model_name),
    tokenizer=RobertaTokenizer.from_pretrained(model_name),
)


emotion_mapping = {
    "admiration": "happy",
    "amusement": "happy",
    "anger": "sad",
    "annoyance": "sad",
    "approval": "happy",
    "caring": "happy",
    "confusion": "sad",
    "curiosity": "happy",
    "desire": "happy",
    "disappointment": "sad",
    "disapproval": "sad",
    "disgust": "sad",
    "embarrassment": "sad",
    "excitement": "happy",
    "fear": "sad",
    "gratitude": "happy",
    "grief": "sad",
    "joy": "happy",
    "love": "happy",
    "nervousness": "sad",
    "optimism": "happy",
    "pride": "happy",
    "realization": "happy",
    "relief": "happy",
    "remorse": "sad",
    "sadness": "sad",
    "surprise": "happy",
    "neutral": "happy",
    
}