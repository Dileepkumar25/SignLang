# 1. Base environment
FROM python:3.10

# 2. Working folder
WORKDIR /app

# 3. Copy project files
COPY . .

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Expose port (Flask default)
EXPOSE 5000

# 6. Run app
CMD ["python", "app.py"]