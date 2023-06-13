FROM python:3.10-alpine

RUN apk add ffmpeg

RUN mkdir /scripts

COPY ./scripts/ /scripts/

RUN pip install subaligner

WORKDIR /scripts

ENTRYPOINT ["python", "/extract_subtitle.py"]
