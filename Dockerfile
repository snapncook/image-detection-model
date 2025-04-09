FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

CMD ["python", "cmd/main.py"]