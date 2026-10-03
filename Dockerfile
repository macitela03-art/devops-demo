# Start from a small, ready-made Python image
FROM python:3.12-slim

# Work inside /app
WORKDIR /app

# Copy the dependency list first so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# The app listens on port 5000
EXPOSE 5000

# Start the app when the container runs
CMD ["python", "app.py"]
