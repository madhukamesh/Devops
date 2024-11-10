from flask import Flask

app = Flask(__name__)

# This is an example of api

@app.get('/')
def index():
    return 'Hello, Welcome to Python flask Server!'

@app.get('/student/<name>')
def get_student(name):
    return {
        "name": name,
        "http_method": "get",
        "server": "sample get method"
    }

@app.get('/probes/startup')
def startup():
    return {
        "status": "ok"
    }


@app.get('/probes/liveness')
def liveness():
    return {
        "status": "ok"
    }

@app.get('/probes/readiness')
def readiness():
    return {
        "status": "ok"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
