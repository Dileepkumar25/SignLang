FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]
