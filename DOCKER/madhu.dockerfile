FROM alpine:latest
WORKDIR /app-docker
COPY . /app-docker
RUN apk update && apk add python3 py3-pip git
ENV husband=kamesh
ENV spouse=madhu
CMD ["python3", "app.py"]
