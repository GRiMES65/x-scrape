from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper import scrape_twitter
from sentiment import analyze_sentiment

app = Flask(__name__)
CORS(app, origins=[
    "https://tweet-mood.vercel.app/"
])

DEFAULT_TWITTER_USER = "elonmusk"  # fallback username

@app.route('/analyze/twitter', methods=['GET'])
def twitter_analysis():
    username = request.args.get('username', DEFAULT_TWITTER_USER)
    tweets = scrape_twitter(username)
    results = analyze_sentiment(tweets)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
