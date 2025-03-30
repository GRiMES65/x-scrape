from flask import Flask, jsonify
from scraper import scrape_twitter
from sentiment import analyze_sentiment

app = Flask(__name__)

TWITTER_USERNAME = "beartestar"
TWITTER_PASSWORD = "Nm4feDGZFsS3uKN"
INSTAGRAM_USERNAME = "your_username"
INSTAGRAM_PASSWORD = "your_password"

@app.route('/analyze/twitter', methods=['GET'])
def twitter_analysis():
    tweets = scrape_twitter(TWITTER_USERNAME, TWITTER_PASSWORD)
    sentiments = analyze_sentiment(tweets)

    # Ensure valid sentiments
    # valid_sentiments = ["Positive", "Negative", "Neutral"]
    # sentiments = [s if s in valid_sentiments else 'Neutral' for s in sentiments]

    sentiment_values = [entry['sentiment'] for entry in sentiments]

    # Count sentiment results
    positive_count  = sum(1 for s in sentiment_values if s == "Positive")
    negative_count  = sum(1 for s in sentiment_values if s == "Negative")
    neutral_count   = sum(1 for s in sentiment_values if s == "Neutral")

    return jsonify({
        "tweets": tweets,
        "sentiments": sentiments,
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count
    })

if __name__ == '__main__':
    app.run(debug=True)
