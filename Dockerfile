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
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Chromium, ChromeDriver, and dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    fonts-liberation \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libxrandr2 \
    libxtst6 \
    xdg-utils \
    && apt-get clean

# Set environment variables for Chromium and ChromeDriver paths
# ENV CHROME_BIN=/usr/bin/chromium
# ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
# ENV PATH="$CHROME_BIN:$CHROMEDRIVER_PATH:$PATH"

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]

