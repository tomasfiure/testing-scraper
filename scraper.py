from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_data(url):
    """
    Scrapes the given URL using Selenium in the prebuilt Docker Selenium container.
    """
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Optional: Use headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        return {"title": driver.title}
    finally:
        driver.quit()
