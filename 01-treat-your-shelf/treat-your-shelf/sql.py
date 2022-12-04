CREATE_BOOKS_TABLE = """
CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title TEXT,
  price_in_pence INT,
  quantity_in_stock INT,
  release_date TEXT,
  is_fiction BOOLEAN
);
"""


GET_AVAILABLE_BOOKS = "SELECT * FROM books;"
