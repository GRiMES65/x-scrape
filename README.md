X-Scrape is a web application that analyzes the sentiment of tweets for a given Twitter handle. It uses a Flask backend for sentiment analysis and a frontend for user interaction.

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



# Deployment Guide

## Frontend Deployment (Vercel)

1. Push your code to GitHub
2. Visit [Vercel](https://vercel.com) and sign in with GitHub
3. Click "New Project" and import your repository
4. Select the frontend directory for deployment
5. Add environment variables:
   ```env
   NEXT_PUBLIC_API_URL=https://your-backend-name.onrender.com
   ```
6. Click "Deploy"

## Backend Deployment (Render)

1. Visit [Render](https://render.com) and create an account
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: `x-scrape-backend` (or your preferred name)
   - Root Directory: `backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. Add environment variables:

   ```env
   PYTHON_VERSION=3.10.0
   PORT=10000
   ```

6. Click "Create Web Service"

## Environment Files

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=https://your-backend-name.onrender.com
```

### Backend (requirements.txt)

First, create requirements.txt in backend directory:

```txt
playwright==1.42.0  # For web scraping
flask==2.0.1
flask-cors==3.0.10
python-dotenv==0.19.0
beautifulsoup4==4.9.3
requests==2.26.0
gunicorn==20.1.0
```

### Backend Setup Steps

1. Create and activate virtual environment:

   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies and setup playwright:

   ```bash
   pip install -r requirements.txt
   playwright install chromium
   playwright install-deps  # Install system dependencies
   ```

3. Configure environment:

   ```bash
   cp .env.example .env
   ```

4. Test the setup:
   ```bash
   python app.py  # Should start the Flask server
   ```

## CORS Configuration

Update your Flask backend to accept requests from your Vercel domain:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[
    "https://your-frontend-name.vercel.app",
    "http://localhost:3000"
])
```

## Deployment Order and Testing

1. Deploy backend first:

   - Push code to GitHub
   - Deploy on Render
   - Wait for build to complete
   - Test API endpoints using the Render URL

2. Deploy frontend:
   - Update NEXT_PUBLIC_API_URL in Vercel
   - Deploy on Vercel
   - Test the complete application

## Monitoring and Logs

- Backend: Use Render dashboard's logs section
- Frontend: Use Vercel's dashboard and analytics

## Troubleshooting

Common issues and solutions:

1. CORS errors:

   - Verify CORS configuration in backend
   - Check if frontend URL is correctly added to allowed origins

2. API connection issues:

   - Confirm backend URL is correct in frontend environment
   - Check if backend service is running on Render
   - Verify API endpoints using Postman or curl

3. Build failures:
   - Check build logs in respective platforms
   - Verify all dependencies are listed in requirements.txt
   - Ensure all environment variables are set correctly

## Important Notes

- Render's free tier will spin down after periods of inactivity
- First request after inactivity may take 30-60 seconds
- For production, consider upgrading to paid tier for better performance

## Repository Setup & Collaboration

### Initial Setup

1. Create a new repository on GitHub
2. Initialize local repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

### Dependencies & Prerequisites

#### System Requirements

1. Python 3.10 or higher
2. Node.js 18 or higher
3. Git

#### Python Dependencies

```bash
pip install playwright  # Required for web scraping
playwright install chromium  # Install browser for scraping
pip install flask==2.0.1
pip install flask-cors==3.0.10
pip install python-dotenv==0.19.0
pip install beautifulsoup4==4.9.3
pip install requests==2.26.0
pip install gunicorn==20.1.0
```

#### Node.js Dependencies

```bash
npm install react@19.0.0
npm install react-dom@19.0.0
npm install next@15.2.4
npm install -D typescript@latest @types/node@latest
npm install -D @types/react@19 @types/react-dom@19
npm install -D tailwindcss@latest @tailwindcss/postcss@latest
```

#### Required Configuration Files

1. Frontend needs:

   - `.env.local` for environment variables
   - `next.config.js` for Next.js configuration
   - `tsconfig.json` for TypeScript configuration
   - `tailwind.config.js` for TailwindCSS

2. Backend needs:
   - `.env` for environment variables
   - `requirements.txt` for Python dependencies

### Quick Setup After Clone

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
