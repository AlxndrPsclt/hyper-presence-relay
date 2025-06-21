FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install Flask
RUN pip install flask flask-cors

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable to ensure output isn't buffered
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "server.py"]

