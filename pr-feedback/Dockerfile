FROM python:3.11-slim

# For running git commands
RUN apt-get update \ 
    && apt-get install -y git curl \
    && apt-get clean

# Install the required packages
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy code files
COPY genai_model.py /genai_model.py
COPY entrypoint.py /entrypoint.py

ENTRYPOINT ["python","/entrypoint.py"]