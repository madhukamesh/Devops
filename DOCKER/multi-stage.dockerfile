# Build stage
FROM alpine:latest AS build-stage
WORKDIR /phython_app
RUN apk update && apk add python3 py3-pip git
COPY . /phython_app

# Copy and Run stage
FROM gcr.io/distroless/python3 AS run-stage
WORKDIR /app
COPY --from=build-stage /phython_app /app
ENTRYPOINT ["python3"]
CMD ["app.py"]
