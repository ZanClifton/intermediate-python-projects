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
