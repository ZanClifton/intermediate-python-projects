import os
import psycopg2
from dotenv import load_dotenv
from sql import INSERT_BOOKS_DATA, INSERT_AUTHORS_DATA

load_dotenv()

database_uri = os.environ["DATABASE_URI"]

connection = psycopg2.connect(database_uri)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(INSERT_BOOKS_DATA)
        cursor.execute(INSERT_AUTHORS_DATA)
