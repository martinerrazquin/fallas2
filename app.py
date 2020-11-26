from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hello():
    return 'Hello, World!'
