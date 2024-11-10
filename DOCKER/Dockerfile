FROM alpine:latest
WORKDIR /phython_app
COPY . /phython_app
RUN apk update && apk add python3 py3-pip git
ENTRYPOINT [ "python3", "app.py"]
