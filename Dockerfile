FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production
ENV PORT=5050

COPY requirements.txt requirements.lock ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python", "main.py"]
