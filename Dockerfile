# Use a small Python base image
FROM python:3.11-slim

# Set working dir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and tests
COPY calculator.py .
COPY tests/ ./tests

# Make the CLI executable
RUN chmod +x calculator.py

# Default command - run the calculator interactively
CMD ["python", "./calculator.py"]
