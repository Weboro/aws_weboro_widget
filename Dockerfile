# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables to avoid warnings and errors
ENV PYTHONUNBUFFERED=1

# Install necessary system packages and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    curl \
    ca-certificates \
    libx11-6 \
    libxkbcommon0 \
    libxrandr2 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxcb1 \
    libdrm2 \
    libgbm1 \
    libvulkan1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libu2f-udev \
    xdg-utils \
    fonts-liberation \
    cron \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    apt-get -f install -y && \
    rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver
RUN LATEST_CHROMEDRIVER_URL=$(curl -sS https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq -r '.channels.Stable.downloads.chromedriver[] | select(.platform == "linux64") | .url') && \
    wget $LATEST_CHROMEDRIVER_URL -O chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin && \
    rm chromedriver_linux64.zip

# Copy everything except what's listed in .dockerignore
COPY . /app

# Set working directory
WORKDIR /app

# Install Python dependencies from the current directory
RUN pip install --no-cache-dir -r requirements.txt

# Copy the cron job configuration
COPY crontab /etc/cron.d/selenium-cron

# Set the permissions for the cron job file
RUN chmod 0644 /etc/cron.d/selenium-cron

# Apply the cron job
RUN crontab /etc/cron.d/selenium-cron

# Create a directory for logs
RUN mkdir /var/log/cron

# Run main.py once and then start cron
CMD ["sh", "-c", "python main.py && cron -f"]
