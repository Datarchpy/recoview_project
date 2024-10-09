from transformers import pipeline

# Hugging Faceの感情分析モデルをロード
sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(review_text):
    result = sentiment_model(review_text)
    return result
