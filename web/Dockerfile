FROM python:3.9-alpine
EXPOSE 5003
WORKDIR /app
COPY * /app/
RUN pip install --quiet --upgrade pip --no-cache-dir -r requirements.txt
CMD python app.py
