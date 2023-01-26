FROM python:3.9

ARG WORKINGENV=/home/fast_api

WORKDIR $WORKINGENV

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt $WORKINGENV

RUN pip install -r requirements.txt

COPY . $WORKINGENV

EXPOSE 8001

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
