FROM python:3.10

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/static

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
