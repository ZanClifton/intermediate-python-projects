import os
import psycopg2
from dotenv import load_dotenv
from art import LOGO
import database

USER_PROMPT = "Welcome to Treat Your Shelf! Please enter your name: "

MENU_PROMPT = """
-- MENU --

1) List available books
99) Exit

Enter your choice: """


def list_available_books(connection):
    books = database.get_available_books(connection)

    for id, title, price_in_pence, quantity_in_stock, release_date, is_fiction, author_id in books:
        print(f"{id}: {title}")


MENU_OPTIONS = {
    "1": list_available_books
}


def menu():
    load_dotenv()
    database_uri = os.environ["DATABASE_URI"]

    connection = psycopg2.connect(database_uri)
    database.create_tables(connection)

    while (selection := input(MENU_PROMPT)) != "99":
        try:
            MENU_OPTIONS[selection](connection)
        except KeyError:
            print("Invalid input selected. Please try again.")


menu()
