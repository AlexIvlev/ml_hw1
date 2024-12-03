FROM python:3.11-alpine

RUN apk add --no-cache \
    build-base \
    g++ \
    gcc \
    libffi-dev \
    musl-dev \
    python3-dev \
    py3-pip

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]