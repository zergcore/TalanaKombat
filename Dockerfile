# Python based image
FROM python:3.9

# workdir container
WORKDIR /app

# Copy all application files inside the container
COPY . /app

# Command to run the script
CMD ["python", "main.py"]