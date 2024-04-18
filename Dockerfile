FROM python:3.12.0

# Create directory for the bot
RUN mkdir /bot && chmod 777 /bot

# Set working directory
WORKDIR /bot

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    pv \
    jq \
    python3-dev \
    ffmpeg \
    mediainfo \
    neofetch \
    fontconfig

# Copy the bot code into the container
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Default command to run the bot
CMD ["bash", "run.sh"]
