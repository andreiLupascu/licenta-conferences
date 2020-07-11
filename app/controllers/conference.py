import json

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.helpers.conference import get_conferences_public, get_sessions_per_conference_private

app = Blueprint("conference", __name__, url_prefix="")


@app.route("/api/conferences", methods=['GET'])
def general_public_get_conferences():
    conferences, status_code = get_conferences_public()
    conference_list = []
    for conference in conferences:
        conference_list.append(json.loads(json.dumps(conference.__dict__)))
    return jsonify({"conferences": conference_list}), status_code


@app.route("/api/conferences/<conference_title>/sessions", methods=['GET'])
@jwt_required
def get_sessions_per_conference(conference_title):
    sessions, status_code = get_sessions_per_conference_private(conference_title)
    return jsonify({"sessions": sessions}), status_code
