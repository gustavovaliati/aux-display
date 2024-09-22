# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the server.py file into the container
COPY server .

# Install the websockets library
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Command to run the server
CMD ["python", "app.py"]
