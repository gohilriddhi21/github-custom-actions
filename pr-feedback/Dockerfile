FROM python:3.11-slim

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY genai_model.py /genai_model.py

COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python","/entrypoint.py"]