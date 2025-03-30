from flask import Flask, jsonify
from scraper import scrape_twitter, scrape_instagram
from sentiment import analyze_sentiment

app = Flask(__name__)

TWITTER_USERNAME = "grimes2865"
TWITTER_PASSWORD = "abCD12><"
INSTAGRAM_USERNAME = "your_username"
INSTAGRAM_PASSWORD = "your_password"

@app.route('/analyze/twitter', methods=['GET'])
def twitter_analysis():
    tweets = scrape_twitter(TWITTER_USERNAME, TWITTER_PASSWORD)
    results = analyze_sentiment(tweets)
    return jsonify(results)

@app.route('/analyze/instagram', methods=['GET'])
def instagram_analysis():
    posts = scrape_instagram(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    results = analyze_sentiment(posts)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
