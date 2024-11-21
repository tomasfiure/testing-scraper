# from flask import Flask, request, jsonify
# from scraper import scrape_data
# import os

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the Selenium Scraping API!"})

# @app.route('/scrape', methods=['POST'])
# def scrape():
#     url = request.json.get('url')
#     if not url:
#         return jsonify({"error": "URL not provided"}), 400
    
#     try:
#         data = scrape_data(url)
#         return jsonify({"data": data})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     port = int(os.getenv('PORT', 8080))
#     app.run(host='0.0.0.0', port=port)

import os
from flask import Flask, request, jsonify
from scraper import scrape_data
import subprocess
app = Flask(__name__)

@app.route('/')
# def home():
#     return jsonify({"message": "Welcome to the Selenium Scraping API!"})
def home():
    try:
        chromium_path = subprocess.run(
            ["which", "chromium"], capture_output=True, text=True, check=True
        ).stdout.strip()
        chromium_version = subprocess.run(
            ["chromium", "--version"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception as e:
        chromium_path = "Chromium not found"
        chromium_version = f"Error: {e}"

    try:
        chromedriver_path = subprocess.run(
            ["which", "chromedriver"], capture_output=True, text=True, check=True
        ).stdout.strip()
        chromedriver_version = subprocess.run(
            ["chromedriver", "--version"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception as e:
        chromedriver_path = "ChromeDriver not found"
        chromedriver_version = f"Error: {e}"

    return jsonify({
        "chromium_path": chromium_path,
        "chromium_version": chromium_version,
        "chromedriver_path": chromedriver_path,
        "chromedriver_version": chromedriver_version,
    })

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL not provided"}), 400

    try:
        data = scrape_data(url)
        return jsonify({"data": data})
    except Exception as e:
        import traceback
        traceback.print_exc()  # Log error for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
