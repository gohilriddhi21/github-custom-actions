FROM python:3.11-slim

RUN apt-get update && apt-get install -y git curl

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.py .

ENTRYPOINT [ "python","entrypoint.py" ]