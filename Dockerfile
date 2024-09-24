# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the server.py file into the container
COPY server/requirements.txt .

# Install the websockets library
RUN pip install -r requirements.txt

COPY server .

# Command to run the server
CMD ["python", "app.py"]
