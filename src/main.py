import flask
from flask import request, jsonify
from git import Repo

app = flask.Flask(__name__)
# version = "1.0"
repo = Repo('.')
assert not repo.bare
commitsha = repo.head.object.hexsha
# tag = reversed(repo.tags)
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
print(tags)
version = latest_tag = tags[-1]
# version = repo.git.tag(l=True)
print(version)
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