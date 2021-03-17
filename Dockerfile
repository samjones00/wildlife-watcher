FROM python:3.7
#FROM ubuntu:16.04
RUN apt-get update ;\
    apt-get install -y tzdata

ENV host:logger:consoleLoggingMode=always

#RUN apt-get update -y && \
#    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]