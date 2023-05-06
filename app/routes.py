from flask import Blueprint
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import os

SELECT_ALL_ARTISTS = "SELECT * FROM artists;"

SELECT_ALL_ACTIVITIES = "SELECT * FROM activities;"

SELECT_ALL_CONCERTS = "SELECT * FROM concerts;"

SELECT_ALL_CALENDAR = "SELECT * FROM calendar;"

main = Blueprint('main', __name__)

@main.get('/')
def home():
    return "Welcome to Raclacamp API"

def get_data_from_db(query):
    url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(url)
    with connection.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(query)
        response = cursor.fetchall()

    json_dump = json.dumps(response, ensure_ascii=False)
    connection.close()
    return json_dump

@main.get('/artists')
def get_artists():
    return get_data_from_db(SELECT_ALL_ARTISTS)

@main.get('/activities')
def get_activities():
    return get_data_from_db(SELECT_ALL_ACTIVITIES)

@main.get('/concerts')
def get_concerts():
    return get_data_from_db(SELECT_ALL_CONCERTS)

@main.get('/calendar')
def get_calendar():
    return get_data_from_db(SELECT_ALL_CALENDAR)

@main.get('/artists/<artistId>')
def get_one_artist(artistId):
    SELECT_ONE_ARTIST = "SELECT * FROM artists WHERE id = {};".format(artistId)
    return get_data_from_db(SELECT_ONE_ARTIST)

@main.get('/activities/<activityId>')
def get_one_activity(activityId):
    SELECT_ONE_ACTIVITY = "SELECT * FROM activities WHERE id = {};".format(activityId)
    return get_data_from_db(SELECT_ONE_ACTIVITY)

@main.get('/concerts/<scene>/<date>')
def get_concerts_scene_date(scene, date):
    SELECT_CONCERTS = "SELECT * FROM concerts WHERE scene = '{}' AND date_day = '{}';".format(scene, date)
    return get_data_from_db(SELECT_CONCERTS)
