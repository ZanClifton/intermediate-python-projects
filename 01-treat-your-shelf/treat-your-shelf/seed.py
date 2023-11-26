import os
import psycopg2
from dotenv import load_dotenv
import sql

load_dotenv()

database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(sql.INSERT_AUTHORS_DATA)
        cursor.execute(sql.INSERT_BOOKS_DATA)
        cursor.execute(sql.INSERT_GENRES_DATA)
        cursor.execute(sql.INSERT_BOOKS_GENRES_DATA)
        cursor.execute(sql.INSERT_REVIEWERS_DATA)
        cursor.execute(sql.INSERT_REVIEWS_DATA)
