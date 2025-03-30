from flask import Flask, jsonify,  request
from scraper import scrape_twitter
from sentiment import analyze_sentiment
from flask_cors import CORS

app = Flask(__name__)


CORS(app)

TWITTER_USERNAME = "beartestar"
TWITTER_PASSWORD = "Nm4feDGZFsS3uKN"
INSTAGRAM_USERNAME = "your_username"
INSTAGRAM_PASSWORD = "your_password"

@app.route('/analyze/twitter', methods=['GET'])
def twitter_analysis():

    username = request.args.get('username')

    if not username:
        return jsonify({"error": "Twitter username is required"}), 400

    tweets = scrape_twitter(TWITTER_USERNAME, TWITTER_PASSWORD, username)
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
        "sentiments": sentiment_values,
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count
    })

if __name__ == '__main__':
    app.run(debug=True)
