from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text_list):
    analyzer = SentimentIntensityAnalyzer()
    results = []

    for text in text_list:
        sentiment_score = analyzer.polarity_scores(text)
        sentiment = "Positive" if sentiment_score['compound'] > 0.05 else "Negative" if sentiment_score['compound'] < -0.05 else "Neutral"
        results.append({"text": text, "sentiment": sentiment})

    return results
