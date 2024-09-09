FROM python:3.11-slim

RUN apt-get update \ 
    && apt-get install -y git curl \
    && apt-get clean

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY vertexai_model.py /vertexai_model.py

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python","/entrypoint.py"]