X-Scrape is a web application that analyzes the sentiment of tweets for a given Twitter handle. It uses a Flask backend for sentiment analysis and a frontend for user interaction.
This app is for educational purposes only.

## Features

- Analyze tweets for positive, neutral, and negative sentiments.
- Display sentiment counts and overall sentiment.
- View individual tweets with their sentiment classification.
- Overall summary of positive/negative percentage.

## Prerequisites

- Python 3.x
- Node.js (if using a Next.js frontend)
- A modern web browser

## AI Usage

This project leverages AI for sentiment analysis using the following components:

1. **VADER Sentiment Analysis:**
   - The backend uses the `vaderSentiment` library, a pre-trained natural language processing tool, to analyze the sentiment of tweets.
   - VADER (Valence Aware Dictionary and sEntiment Reasoner) is specifically designed to handle social media text, making it ideal for analyzing tweets.
   - It classifies each tweet as **Positive**, **Neutral**, or **Negative** based on its sentiment score.

2. **Playwright for Web Scraping:**
   - Playwright, an automation library, is used to scrape tweets from Twitter profiles.
   - While not strictly an AI, Playwright uses advanced algorithms to simulate human-like interactions with web pages, such as scrolling, clicking, and waiting for dynamic content to load.
   - This enables the application to retrieve tweets efficiently, even from dynamically loaded content.

3. **Sentiment Classification:**
   - Each tweet is classified as **Positive**, **Neutral**, or **Negative** based on its sentiment score.
   - The overall sentiment for the Twitter handle is determined by aggregating the sentiment scores of all analyzed tweets.

4. **Real-Time Analysis:**
   - The AI model processes tweets in real-time, providing instant feedback to the user. However, it processes random tweets and not most recent tweets.

This AI-powered approach ensures accurate and efficient sentiment analysis tailored for social media data.

## Usage

1. Open the frontend in your browser.
2. Enter a Twitter handle (e.g., `@NASA`) in the input field.
3. Click "Analyze" to view sentiment analysis results.

## Quick Setup After Clone

```bash
# Clone repository
git clone <repo-url>
cd new-project-name

# Setup backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env

# Setup frontend
cd ../frontend
npm install
cp .env.example .env.local
```

### For Collaborators

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd new-project-name  # Changed from x-scrape-test
   ```

2. Frontend setup:

   ```bash
   cd frontend
   npm install
   cp .env.example .env.local    # Create your local env file
   ```

3. Backend setup:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env     # Create your local env file
   ```

### Environment Files Setup

Each developer needs to set up their own environment files:

1. Frontend (.env.local):

   ```env
   NEXT_PUBLIC_API_URL=http://localhost:5000  # For local development
   ```

2. Backend (.env):
   ```env
   PORT=5000
   DEBUG=True
   ```

### Branch Management

- Create feature branches from main:
  ```bash
  git checkout -M feature/your-feature-name
  ```
- Keep main branch deployable at all times
- Use pull requests for code review

### Important Git Files

- .gitignore is already set up to exclude:
  - Node modules
  - Python virtual environment
  - Environment files
  - Build directories

## Development Workflow

1. Always pull latest changes:
   ```bash
   git pull origin main
   ```
2. Install dependencies if package.json or requirements.txt changed
3. Update your .env files if new variables were added
4. Create feature branch
5. Make changes
6. Push changes and create pull request
