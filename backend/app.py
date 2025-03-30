from flask import Flask, jsonify
from scraper import scrape_twitter, scrape_instagram
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
    # valid_sentiments = ['positive', 'negative', 'neutral']
    # sentiments = [s if s in valid_sentiments else 'Neutral' for s in sentiments]

    # Count sentiment results
    positive_count = sum(1 for s in sentiments if s == "Positive")
    negative_count = sum(1 for s in sentiments if s == "Negative")
    neutral_count = sum(1 for s in sentiments if s == "Neutral")

    return jsonify({
        "tweets": tweets,
        "sentiments": sentiments,
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count
    })

@app.route('/analyze/instagram', methods=['GET'])
def instagram_analysis():
    posts = scrape_instagram(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    results = analyze_sentiment(posts)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
