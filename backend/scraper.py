from playwright.sync_api import sync_playwright
import time
import random

def scrape_twitter(target_username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0',
            viewport={'width': 1280, 'height': 1024}
        ).new_page()
        
        try:
            # Go to user's profile and ensure full load
            page.goto(f'https://twitter.com/{target_username}', wait_until='domcontentloaded')
            page.wait_for_selector('[data-testid="primaryColumn"]', timeout=15000)
            time.sleep(2)  # Extra wait for dynamic content
            
            # Scroll more times to ensure latest tweets
            for _ in range(5):
                page.evaluate('window.scrollBy(0, 800)')
                time.sleep(1)
                page.wait_for_load_state('networkidle')

            # Get tweets with enhanced selector to exclude pinned tweets
            tweets = page.eval_on_selector_all(
                '[data-testid="tweet"]:not([data-testid="pinned-tweet"])',
                '''elements => elements.map(el => {
                    const tweetText = el.querySelector('[data-testid="tweetText"]');
                    const time = el.querySelector('time');
                    if (!tweetText || !time) return null;
                    return {
                        text: tweetText.textContent,
                        date: time.getAttribute('datetime')
                    };
                }).filter(item => item !== null)'''
            )
            
            # Sort by date and get latest tweets
            sorted_tweets = sorted(
                [t for t in tweets if t['text'].strip()],
                key=lambda x: x['date'],
                reverse=True
            )
            
            return [t['text'] for t in sorted_tweets[:15]]
            
        except Exception as e:
            print(f"Error scraping tweets from {target_username}: {str(e)}")
            return []
            
        finally:
            browser.close()
