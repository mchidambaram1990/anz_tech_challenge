import flask
from flask import request, jsonify
from git import Repo


def get_git_data():
    repo = Repo('.')
    # assert not repo.bare

   # if repo.bare:
    #    raise git.exc.InvalidGitRepositoryError

    # retrive the latest commit sha
    commitsha = repo.head.object.hexsha

    # retrive all the tags and sort in descending order
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    version = str(tags[-1])

    return version, commitsha


def api_json_object():
    version, commitsha = get_git_data()
    gitData = [
        {
            "version": version,
            "lastcommitsha": commitsha,
            "description": "pre interview technical test"
        }
    ]

    return gitData


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1> ANZ pre Interview Solution</h1> <p> <p><a href=../version>click here to navigate to /version page</a></p></p>"


# returns the version and commit sha data
@app.route('/version', methods=['GET'])
def git_version():
    return jsonify(api_json_object())


app.run(debug=True,host='0.0.0.0')
#app.run()

