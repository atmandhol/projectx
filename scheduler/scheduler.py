import json
from flask import Flask
from flask import make_response
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/ping', methods=['GET'])
def index():
    resp = make_response(json.dumps({"message": "Hello from Project X!"}))
    return resp

