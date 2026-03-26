FROM python:3.10

WORKDIR /app

# ✅ Install system dependencies (FIX)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

# Copy requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]