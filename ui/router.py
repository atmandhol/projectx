from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return open("ui/dashboard.html").read()
