FROM python:3.12-slim
WORKDIR /app

RUN apt-get update \
    && apt-get upgrade \ 
    && apt-get install -y \
    default-mysql-client \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install mysqlclient
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
