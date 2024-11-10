FROM python:3.12.4-slim
WORKDIR /flask_app
COPY . /flask_app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python3", "demo-server.py"]
