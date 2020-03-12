FROM python:3.7-alpine

COPY requirements.txt requirements.txt

RUN apk --no-cache add --virtual=.build-dep build-base \
    && apk --no-cache add bash g++ zeromq-dev libffi-dev \
    && pip install -r requirements.txt \
    && apk del .build-dep

EXPOSE 5557 5558 8089

ENTRYPOINT ["locust"] 