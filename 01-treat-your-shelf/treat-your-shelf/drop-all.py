import os
import psycopg2
from dotenv import load_dotenv
import sql

load_dotenv()

database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(sql.DROP_BOOKS_TABLE)
        cursor.execute(sql.DROP_AUTHORS_TABLE)
        cursor.execute(sql.DROP_GENRES_TABLE)
        cursor.execute(sql.DROP_BOOKS_GENRES_TABLE)
        cursor.execute(sql.DROP_REVIEWERS_TABLE)
        cursor.execute(sql.DROP_REVIEWS_TABLE)
