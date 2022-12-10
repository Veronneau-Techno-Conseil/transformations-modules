FROM python:3.9-bullseye
COPY ./requirements.txt ./
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

ENV ACTION="configure"
ENV CONFIG="/data/config.json"
ENV DATA="/data/data.json"

WORKDIR /scripts
COPY ./*.py ./
COPY requirements.txt ./

ENTRYPOINT python3 app.py --action=$ACTION --config=$CONFIG --data=$DATA