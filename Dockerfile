FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# Copy project files into the image
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# This will run when container starts
CMD ["python", "main.py"]
