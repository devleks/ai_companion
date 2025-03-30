# Use a specific Python version from Docker Hub
FROM python:3.8.18-slim-bullseye

# Set working directory in container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a directory for storing conversation history and memory
RUN mkdir -p /app/data

# Install bash
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Environment variables
ENV PYTHONUNBUFFERED=1

# Set bash as the default shell
SHELL ["/bin/bash", "-c"]

# Command to keep container running
CMD ["bash"]
