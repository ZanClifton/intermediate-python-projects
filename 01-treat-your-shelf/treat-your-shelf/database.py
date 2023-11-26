import sql

# CREATE


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.CREATE_BOOKS_TABLE)
            cursor.execute(sql.CREATE_AUTHORS_TABLE)
            cursor.execute(sql.CREATE_GENRES_TABLE)
            cursor.execute(sql.CREATE_BOOKS_GENRES_TABLE)
            cursor.execute(sql.CREATE_REVIEWERS_TABLE)
            cursor.execute(sql.CREATE_REVIEWS_TABLE)

# SELECT *


def get_available_books(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.GET_AVAILABLE_BOOKS)
            return cursor.fetchall()


def get_authors(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.GET_AUTHORS)
            return cursor.fetchall()


def get_available_genres(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.GET_AVAILABLE_GENRES)
            return cursor.fetchall()


def get_all_reviewers(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.GET_ALL_REVIEWERS)
            return cursor.fetchall()


def get_all_reviews(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.GET_ALL_REVIEWS)
            return cursor.fetchall()
