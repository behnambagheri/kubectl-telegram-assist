# Use a lightweight official Python image
FROM python:3.13-slim

# Set the PYTHONUNBUFFERED to ensure immediate log output
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONFAULTHANDLER=1

# Set a working directory inside the container
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt /app/requirements.txt

# Install the necessary Python packages efficiently
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Use a non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Set entrypoint for better signal handling
ENTRYPOINT ["python"]
CMD ["main.py"]