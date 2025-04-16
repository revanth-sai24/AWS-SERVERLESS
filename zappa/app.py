import awsgi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/test')
def hello_world():
    return 'testing, World!'


def handler(event, context):
    return awsgi.response(app, event, context)
