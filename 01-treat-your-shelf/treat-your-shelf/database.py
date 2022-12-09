import sql


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.CREATE_BOOKS_TABLE)
            cursor.execute(sql.CREATE_AUTHORS_TABLE)
            cursor.execute(sql.CREATE_GENRES_TABLE)
            cursor.execute(sql.CREATE_BOOKS_GENRES_TABLE)
            cursor.execute(sql.CREATE_REVIEWERS_TABLE)
            cursor.execute(sql.CREATE_REVIEWS_TABLE)


def get_available_books(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql.GET_AVAILABLE_BOOKS)
            return cursor.fetchall()
