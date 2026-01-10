FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    Flask_app=main.py

WORKDIR /app

COPY app .

RUN apt-get --no-cache-dir upgrade && apt-get --no-cache-dir upgrade \
    && apt-get install -y mysql-client \
    pip install mysql \
    pip install mysql-connector-python

COPY . .

RUN pip install --system -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

