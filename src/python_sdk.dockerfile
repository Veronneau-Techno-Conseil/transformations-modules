FROM mcr.microsoft.com/vscode/devcontainers/python:3.9-bullseye
COPY ./requirements.txt ./
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN /usr/local/bin/python3 -m pip install --upgrade pylint