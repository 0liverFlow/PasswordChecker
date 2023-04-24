FROM python:3

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y xclip libx11-dev libxtst-dev libxkbfile-dev

RUN pip install -r requirements.txt

CMD ["python3", "./PasswordChecker.py"]
