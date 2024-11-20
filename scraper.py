from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrape_data(url):
    # Set Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        # Example: Extract title of the webpage
        title = driver.title
        return {"title": title}
    finally:
        driver.quit()
