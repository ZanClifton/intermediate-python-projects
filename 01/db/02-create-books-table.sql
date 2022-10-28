\c treat_your_shelf;

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title TEXT,
  price_in_pence INT,
  quantity_in_stock INT,
  release_date TEXT,
  is_fiction BOOLEAN
);