FROM python:3.7-slim-buster

RUN apt -y update && apt install -y --no-install-recommends \
    libgomp1 \
    && apt clean    

COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY code /app

ENV PYTHONUNBUFFERED=TRUE

WORKDIR /app

RUN chmod +x run.sh
CMD ["python3", "run.sh"]
