import json

from flask import Blueprint, jsonify

from app.helpers.conference import get_conferences_public

app = Blueprint("conference", __name__, url_prefix="")


@app.route("/api/conferences", methods=['GET'])
def general_public_get_conferences():
    conferences, status_code = get_conferences_public()
    conference_list = []
    for conference in conferences:
        conference_list.append(json.loads(json.dumps(conference.__dict__)))
    return jsonify({"conferences": conference_list}), status_code
