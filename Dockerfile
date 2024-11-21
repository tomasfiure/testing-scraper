# # Base image with Python and Chrome
# FROM python:3.11

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     wget \
#     unzip \
#     libnss3 \
#     libgconf-2-4 \
#     libxi6 \
#     libxrender1 \
#     libxrandr2 \
#     libxtst6 \
#     xdg-utils \
#     fonts-liberation \
#     && apt-get clean

# # Install Chromium and ChromeDriver dependencies
# RUN apt-get update && apt-get install -y \
#     chromium \
#     chromium-driver \
#     fonts-liberation \
#     && apt-get clean
    
# # Install Chrome WebDriver
# # RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
# #     && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
# #     && chmod +x /usr/local/bin/chromedriver

# # # Install Chrome browser
# # RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
# #     && echo "deb [signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
# #     && apt-get update \
# #     && apt-get install -y google-chrome-stable \
# #     && apt-get clean

# # Set the working directory
# WORKDIR /app

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy application files
# COPY . .

# # Expose port and set command
# EXPOSE 8080
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]

# Use the official Python image
# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install Chromium, ChromeDriver, and dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    fonts-liberation \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libxrandr2 \
    libxtst6 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    xdg-utils \
    && apt-get clean

# Verify Chromium and ChromeDriver installation during build
# RUN echo "Verifying Chromium installation during build:" && which chromium || which chromium-browser
# RUN echo "Chromium Version:" && chromium --version || echo "Chromium not found!"
# RUN echo "ChromeDriver Version:" && chromedriver --version || echo "ChromeDriver not found!"

# # Set environment variables for Chromium and ChromeDriver paths
ENV CHROME_BIN=/usr/bin/chromium
# ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
# ENV PATH="/usr/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the app's port
EXPOSE 8080

# Add runtime checks for Chromium and ChromeDriver
CMD echo "Runtime check: Chromium Path:" && which chromium || echo "Chromium not found" \
    && echo "Runtime check: ChromeDriver Path:" && which chromedriver || echo "ChromeDriver not found" \
    && gunicorn --bind 0.0.0.0:8080 main:app


