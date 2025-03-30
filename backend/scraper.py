from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_twitter(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)
    target_handle = 'BillGates'
    max_tweets = 3

    try:
        driver.get("https://twitter.com/i/flow/login")
        
        # Enter username and click next
        username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        username_input.send_keys(username)
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
        next_button.click()
        
        # Enter password
        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        password_input.send_keys(password)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']")))
        login_button.click()
    
        # Navigate to the target profile
        driver.get(f"https://twitter.com/{target_handle}")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article[data-testid="tweet"]')))

        tweets = []
        last_height = driver.execute_script("return document.body.scrollHeight")

        while len(tweets) < max_tweets:
            # Extract tweets using BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")
            new_tweets = [tweet.text for tweet in soup.find_all("div", {"data-testid": "tweetText"})]
            
            # Add only unique tweets
            for tweet in new_tweets:
                if tweet not in tweets:
                    tweets.append(tweet)
                    if len(tweets) >= max_tweets:
                        break

            # Scroll down to load more tweets
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Adjust if needed

            # Check if the scroll reached the end
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Get tweets
        # soup = BeautifulSoup(driver.page_source, "html.parser")
        # tweets = [tweet.text for tweet in soup.find_all("div", {"data-testid": "tweetText"})]
        #tweets = scrape_twitter('your_username', 'your_password', 'elonmusk')
        
        return tweets[:max_tweets]
    
    except Exception as e:
        print(f"Error scraping Twitter: {str(e)}")
        return []
    finally:
        driver.quit()

from playwright.sync_api import sync_playwright

def scrape_instagram(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.instagram.com/accounts/login/")
        page.wait_for_timeout(5000)

        page.fill("input[name='username']", username)
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")
        page.wait_for_timeout(5000)

        page.goto(f"https://www.instagram.com/{username}/")
        page.wait_for_timeout(5000)

        posts = page.locator("article div div div div a").all_text_contents()

        browser.close()
        return posts[:15]
