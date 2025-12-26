# ---------- Base Image ----------
FROM python:3.12-slim

# Install nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# ---------- Backend Setup ----------
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app.py /app/app.py

# ---------- Frontend Setup ----------
COPY frontend/ /var/www/html/

# ---------- Nginx Config ----------
COPY nginx.conf /etc/nginx/nginx.conf

# ---------- Expose Port ----------
EXPOSE 80

# ---------- Start Both ----------
CMD service nginx start && gunicorn -w 4 -b 127.0.0.1:5000 app:app

