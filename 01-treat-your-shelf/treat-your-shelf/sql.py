# Create Tables

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

CREATE_AUTHORS_TABLE = """
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    author_name TEXT,
    fun_fact TEXT
);
"""


# Select Queries

GET_AVAILABLE_BOOKS = "SELECT * FROM books;"

# Populate Tables

INSERT_BOOKS_DATA = """INSERT INTO books (title, price_in_pence, quantity_in_stock, release_date, is_fiction)
VALUES 
    ('The Hitchhiker''s Guide to the Galaxy', 599, 100, '1979-10-12', true),
    ('The Restaurant at the End of the Universe', 599, 100, '1980-10-12', true),
    ('The Little Prince', 699, 1020, '1943-04-06', true),
    ('The Tale of Peter Rabbit', 599, 1000, '1902-10-01', true),
    ('Emma', 522, 390, 	'1815-12-23', true),
    ('Nineteen Eighty-Four: A Novel', 799, 420, '1949-06-08', true),
    ('The Handmaid''s Tale', 899, 10, '1985-08-01' ,true),
    ('The War of the Worlds', 250, 17, '1897-04-01', true),
    ('Captain Corelli''s Mandolin', 999, 0, '1995-08-29', true),
    ('A Brief History of Time', 825, 0, '1988-04-01', false),
    ('Pride and Prejudice', 699, 4, '1813-01-28', true),
    ('The Gremlins', 499, 125, '1943', true),
    ('Sometime Never: A Fable for Supermen', 699, 324, '1948', true),
    ('James and the Giant Peach', 499, 82, '1961', true),
    ('Charlie and the Chocolate Factory', 499, 58, '1964', true),
    ('The Magic Finger', 499, 22, '1966', true),
    ('Fantastic Mr Fox', 499, 5, '1970', true),
    ('Charlie and the Great Glass Elevator', 499, 9, '1972', true),
    ('Danny, the Champion of the World', 499, 100, '1975', true),
    ('The Twits', 499, 120, '1980', true),
    ('George''s Marvellous Medicine', 499, 7, '1981', true),
    ('The BFG', 499, 21, '1982', true),
    ('The Witches', 499, 20, '1983', true),
    ('Matilda', 499, 20, '1988', true),
    ('Tales of the Unexpected', 499, 20, '1979', true),
    ('Life, the Universe and Everything', 799, 100, '1982', true),
    ('So Long, and Thanks for All the Fish', 799, 100, '1984', true),
    ('Dirk Gently''s Holistic Detective Agency', 799, 100, '1987', true),
    ('The Long Dark Tea-Time of the Soul', 799, 99, '1988', true),
    ('Mostly Harmless', 799, 100, '1992', true),
    ('The Illustrated Hitchhiker''s Guide to the Galaxy', 1299, 10, '1994', true),
    ('The Salmon of Doubt', 899, 100, '2002', true);"""

INSERT_AUTHORS_DATA = """INSERT INTO authors (author_name, fun_fact)
VALUES
    ('Dan Brown', 'His favourite colour is not brown'),
    ('Antoine de Saint-Exupéry', 'He was a successful commercial pilot before World War II, working airmail routes in Europe, Africa, and South America.'),
    ('Douglas Adams', 'He made two appearances in Monty Python''s Flying Circus'),
    ('Stephen Hawking', 'Doctors told him he wouldn''t live past his early 20s'),
    ('Eric Carle', 'When he was a young boy, Carle had a dream that he would build a bridge from Germany to America.'),
    ('J. D. Salinger', 'The Catcher in the Rye was the only novel that J.D. Salinger published during his lifetime, not bad for a first try!'),
    ('Beatrix Potter', 'Between 1881 and 1897 Potter kept a journal in which she jotted down her private thoughts in a secret code . This code was so fiendishly difficult it was not cracked and translated until 1958.'),
    ('C. S. Lewis', 'Lewis set up a charitable trust to give away whatever money he received from his books.'),
    ('Roald Dahl', 'During World War II he passed intelligence to MI6 from Washington.'),
    ('Frank Herbert', 'While conversing with fungi expert Paul Stamets, Herbert revealed that the world of Dune was influenced by the lifecycle of mushrooms, with his imagination being helped along by a more "magic" variety.'),
    ('Louis de Bernières', 'De Bernières is an avid musician who plays flute, mandolin, clarinet and guitar.'),
    ('H. G. Wells', 'In 1914 H.G. Wells published a novel titled The World Set Free. In this book he described a weapon that was eerily similar to the first atomic bomb unleashed on the Japanese cities of Hiroshima and Nagasaki in 1945.'),
    ('George Orwell', 'Orwell intentionally got himself arrested for being "drunk and incapable."'),
    ('Jane Austen', 'The author of her first novel, Sense and Sensibility was simply "A Lady," and her later works like Pride and Prejudice were credited to "the Author of Sense and Sensibility." She wasn''t named as the author of her novels until after her death!'),
    ('Margaret Atwood', 'Atwood was the first author to contribute to The Future Library Project, which will take one writer''s contribution each year for one hundred years to be printed in the year 2114.');"""
