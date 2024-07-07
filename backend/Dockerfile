# Use a Python 3.12 base image
FROM python:3.12-alpine

# Install system dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-dev \
    pkgconfig

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt


# Copy the rest of the application code
COPY . /app


# Collect static files
RUN python manage.py collectstatic --noinput

# Copy the .env file to the container
COPY .env /app/.env

# Make startup.sh executable
RUN chmod +x /app/startup.sh

# Command to run the application
CMD ["/bin/sh", "-c", "/app/startup.sh"]
