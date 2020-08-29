import flask
from flask import request, jsonify
# from git import Repo

app = flask.Flask(__name__)
version = "1.0"
commitsha = "acvbkwjefjpkwef"

gitData = [
    {
        "version" : version,
        "lastcommitsha" : commitsha,
        "description" : "pre interview technical test"
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1> ANZ pre Interview Solution</h1>"

@app.route('/version', methods=['GET'])
def git_version():
    return jsonify(gitData)

app.run()