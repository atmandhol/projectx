import json
from flask import Flask
from flask import make_response
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/work', methods=['GET'])
def index():
    resp = make_response(json.dumps({"message": "Worker will start doing work here based on task"}))
    return resp

