import os
import json

from flask import Flask
from flask import make_response
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/manager/showTasks', methods=['GET'])
def show_tasks():
    resp = make_response(json.dumps({"message": "Nothing to see here!"}))
    return resp
