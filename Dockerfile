FROM python:3.9.5

ENV DEBUG=1

WORKDIR /opt/backend

RUN apt -y update && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt

CMD python -m uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload