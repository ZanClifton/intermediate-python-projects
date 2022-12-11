import os
import psycopg2
from dotenv import load_dotenv
from art import LOGO
import database as db

USER_PROMPT = "Welcome to Treat Your Shelf! Please enter your name: "

MENU_PROMPT = """
-- MENU --

1) List available books
2) List authors on file
3) List available genres
4) List all reviewers
5) Show all reviews
99) Exit

Enter your choice: """


def list_available_books(connection):
    books = db.get_available_books(connection)

    for id, title, price_in_pence, quantity_in_stock, release_date, is_fiction, author_id in books:
        print(f"""{id}: {title}""")


def list_authors(connection):
    authors = db.get_authors(connection)

    for id, author_name, fun_fact in authors:
        print(f"""
{id}: {author_name} 
Fun Fact: {fun_fact}
""")


def list_available_genres(connection):
    genres = db.get_available_genres(connection)

    for id, genre in genres:
        print(f"{genre.capitalize()}")


def list_all_reviewers(connection):
    reviewers = db.get_all_reviewers(connection)

    for id, username, first_name, last_name, email, fave_genre_id, fave_book_id in reviewers:
        print(f"""
{id}: {username}
""")


def list_all_reviews(connection):
    reviews = db.get_all_reviews(connection)

    for id, book_id, review_title, review_body, rating, reviewer_id in reviews:
        print(f"""
{review_title}
{review_body}
""")


MENU_OPTIONS = {
    "1": list_available_books,
    "2": list_authors,
    "3": list_available_genres,
    "4": list_all_reviewers,
    "5": list_all_reviews
}


def menu():
    load_dotenv()
    database_uri = os.environ["DATABASE_URI"]

    connection = psycopg2.connect(database_uri)
    db.create_tables(connection)

    while (selection := input(MENU_PROMPT)) != "99":
        try:
            MENU_OPTIONS[selection](connection)
        except KeyError:
            print("Invalid input selected. Please try again.")


menu()
