# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Install any necessary dependencies (none required here, but you can add them if needed)
RUN pip install --no-cache-dir --upgrade pip

# Run the Python script when the container starts
CMD ["python", "app.py"]
