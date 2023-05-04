from flask import Blueprint
import json
import psycopg2
import os

SELECT_ALL_ARTISTS = (
    "SELECT * FROM artists;"
)

main = Blueprint('main', __name__)

@main.get('/')
def home():
    return "Welcome to Raclacamp API"

@main.get('/artists')
def get_artists():
    url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(url)
    with connection.cursor() as cursor:
        cursor.execute(SELECT_ALL_ARTISTS)
        response = cursor.fetchall()

    json_dump = json.dumps(response, ensure_ascii=False)
    connection.close()
    return json_dump