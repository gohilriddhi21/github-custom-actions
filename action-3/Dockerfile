FROM python:3.11-slim

RUN apt-get update \ 
    && apt-get install -y git curl \
    && apt-get clean

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python","/entrypoint.py"]