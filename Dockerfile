FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]




