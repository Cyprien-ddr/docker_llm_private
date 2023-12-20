FROM python:3.9.18-slim-bullseye
WORKDIR /home
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirement.txt
RUN pip install -r ./requirement.txt
COPY ./app ./app
EXPOSE 3000
