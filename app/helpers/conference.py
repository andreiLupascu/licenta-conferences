import datetime
from datetime import datetime
import json
import pymysql
from flask import jsonify

from app.common.models import Conference
from app.helpers.database import get_connection
from app.helpers.extensions import mongo


def get_conferences_public():
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cur:
        try:
            cur.execute(
                "SELECT title, path_to_logo, location, path_to_description, country, start_date, end_date FROM conference")
            result_rows = cur.fetchall()
            conferences = []
            for row in result_rows:
                conferences.append(Conference(
                    row['title'],
                    row['path_to_logo'],
                    row['location'],
                    row['path_to_description'],
                    row['country'],
                    datetime.timestamp(row['start_date']),
                    datetime.timestamp(row['end_date'])))
            return conferences, 200
        except KeyError:
            return jsonify({"msg": "Error getting conferences."}), 400


def get_sessions_per_conference_private(conference_title):
    session_cursor = mongo.db.session.find({"conferenceTitle": conference_title}, {'_id': False})
    sessions = []
    for entry in session_cursor:
        sessions.append(entry)
    return sessions, 200
