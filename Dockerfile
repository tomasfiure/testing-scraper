# Use the official Selenium Standalone Chrome image
FROM selenium/standalone-chrome:latest

# Set the working directory
WORKDIR /app

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean

# Copy application files
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port for Flask (optional)
EXPOSE 8080

# Start the Flask app
CMD ["python3", "main.py"]
