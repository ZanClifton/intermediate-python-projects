# Create Tables

CREATE_AUTHORS_TABLE = """
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    author_name TEXT,
    fun_fact TEXT
);
"""

CREATE_BOOKS_TABLE = """
CREATE TABLE IF NOT EXISTS books (
  id SERIAL PRIMARY KEY,
  title TEXT,
  price_in_pence INT,
  quantity_in_stock INT,
  release_date TEXT,
  is_fiction BOOLEAN,
  author_id INT
);
"""

CREATE_BOOKS_GENRES_TABLE = """
CREATE TABLE IF NOT EXISTS books_genres (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id) ON DELETE CASCADE,
    genre_id INTEGER REFERENCES genres(id) ON DELETE CASCADE
);
"""

CREATE_GENRES_TABLE = """
CREATE TABLE IF NOT EXISTS genres (
    id SERIAL PRIMARY KEY,
    genre VARCHAR(32)
);
"""

CREATE_REVIEWERS_TABLE = """
CREATE TABLE IF NOT EXISTS reviewers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    fave_genre_id INT,
    fave_book_id INT
);
"""

CREATE_REVIEWS_TABLE = """
CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    review_title TEXT,
    review_body TEXT,
    rating INTEGER NOT NULL,
    reviewer_id INTEGER NOT NULL
);
"""


# Drop Tables

DROP_AUTHORS_TABLE = "DROP TABLE IF EXISTS authors;"
DROP_BOOKS_GENRES_TABLE = "DROP TABLE IF EXISTS books_genres;"
DROP_BOOKS_TABLE = "DROP TABLE IF EXISTS books;"
DROP_GENRES_TABLE = "DROP TABLE IF EXISTS genres;"
DROP_REVIEWERS_TABLE = "DROP TABLE IF EXISTS reviewers;"
DROP_REVIEWS_TABLE = "DROP TABLE IF EXISTS reviews;"


# Select Queries
# SELECT *

GET_AVAILABLE_BOOKS = "SELECT * FROM books;"
GET_AUTHORS = "SELECT * FROM authors;"
GET_AVAILABLE_GENRES = "SELECT * FROM genres;"
GET_ALL_REVIEWERS = "SELECT * FROM reviewers;"
GET_ALL_REVIEWS = "SELECT * FROM reviews;"

# Populate Tables

INSERT_BOOKS_DATA = """
INSERT INTO books (title, price_in_pence, quantity_in_stock, release_date, is_fiction, author_id)
VALUES 
    ('The Hitchhiker''s Guide to the Galaxy', 599, 100, '1979-10-12', true, 3),
    ('The Restaurant at the End of the Universe', 599, 100, '1980-10-12', true, 3),
    ('The Little Prince', 699, 1020, '1943-04-06', true, 2),
    ('The Tale of Peter Rabbit', 599, 1000, '1902-10-01', true, 7),
    ('Emma', 522, 390, 	'1815-12-23', true, 14),
    ('Nineteen Eighty-Four: A Novel', 799, 420, '1949-06-08', true, 13),
    ('The Handmaid''s Tale', 899, 10, '1985-08-01' ,true, 15),
    ('The War of the Worlds', 250, 17, '1897-04-01', true, 12),
    ('Captain Corelli''s Mandolin', 999, 0, '1995-08-29', true, null),
    ('A Brief History of Time', 825, 0, '1988-04-01', false, null),
    ('Pride and Prejudice', 699, 4, '1813-01-28', true, 14),
    ('The Gremlins', 499, 125, '1943', true, 9),
    ('Sometime Never: A Fable for Supermen', 699, 324, '1948', true, 9),
    ('James and the Giant Peach', 499, 82, '1961', true, 9),
    ('Charlie and the Chocolate Factory', 499, 58, '1964', true, 9),
    ('The Magic Finger', 499, 22, '1966', true, 9),
    ('Fantastic Mr Fox', 499, 5, '1970', true, 9),
    ('Charlie and the Great Glass Elevator', 499, 9, '1972', true, 9),
    ('Danny, the Champion of the World', 499, 100, '1975', true, 9),
    ('The Twits', 499, 120, '1980', true, 9),
    ('George''s Marvellous Medicine', 499, 7, '1981', true, 9),
    ('The BFG', 499, 21, '1982', true, 9),
    ('The Witches', 499, 20, '1983', true, 9),
    ('Matilda', 499, 20, '1988', true, 9),
    ('Tales of the Unexpected', 499, 20, '1979', true, 9),
    ('Life, the Universe and Everything', 799, 100, '1982', true, 3),
    ('So Long, and Thanks for All the Fish', 799, 100, '1984', true, 3),
    ('Dirk Gently''s Holistic Detective Agency', 799, 100, '1987', true, 3),
    ('The Long Dark Tea-Time of the Soul', 799, 99, '1988', true, 3),
    ('Mostly Harmless', 799, 100, '1992', true, 3),
    ('The Illustrated Hitchhiker''s Guide to the Galaxy', 1299, 10, '1994', true, 3),
    ('The Salmon of Doubt', 899, 100, '2002', true, 3);
"""

INSERT_AUTHORS_DATA = """
INSERT INTO authors (author_name, fun_fact)
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
    ('George Orwell', 'Orwell intenionally got himself arrested for being "drunk and incapable."'),
    ('Jane Austen', 'The author of her first novel, Sense and Sensibility was simply "A Lady," and her later works like Pride and Prejudice were credited to "the Author of Sense and Sensibility." She wasn''t named as the author of her novels until after her death!'),
    ('Margaret Atwood', 'Atwood was the first author to contribute to The Future Library Project, which will take one writer''s contribution each year for one hundred years to be printed in the year 2114.');
"""

INSERT_GENRES_DATA = """
INSERT INTO genres (genre)
VALUES 
    ('adventure'),
    ('children''s'),
    ('classics'),
    ('comedy'),
    ('dystopian'),
    ('fantasy'),
    ('historical-fiction'),
    ('horror'),
    ('mystery'),
    ('nonfiction'),
    ('paranormal'),
    ('romance'),
    ('science'),
    ('sci-fi'),
    ('thriller'),
    ('young adult');
"""

INSERT_BOOKS_GENRES_DATA = """
INSERT INTO books_genres (book_id, genre_id)
VALUES
    (1, 1),
    (1, 4),
    (1, 14),
    (2, 1),
    (2, 4),
    (2, 14),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 2),
    (4, 3),
    (5, 3),
    (5, 12),
    (6, 3),
    (6, 5),
    (6, 14),
    (7, 5),
    (8, 3),
    (8, 14),
    (9, 7),
    (9, 12),
    (10, 10),
    (10, 13),
    (11, 3),
    (11, 12),
    (12, 1),
    (12, 2),
    (12, 6),
    (13, 1),
    (13, 6),
    (14, 1),
    (14, 2),
    (14, 6),
    (15, 1),
    (15, 2),
    (15, 6),
    (16, 2),
    (17, 2),
    (17, 6),
    (18, 1),
    (18, 2),
    (18, 6),
    (19, 1),
    (19, 2),
    (19, 1),
    (19, 2),
    (19, 6),
    (20, 2),
    (21, 2),
    (22, 2),
    (23, 2),
    (24, 2),
    (25, 6),
    (25, 11),
    (25, 14),
    (26, 1),
    (26, 4),
    (26, 14),
    (27, 1),    
    (27, 4),
    (27, 14),
    (28, 1),
    (28, 4),
    (28, 14),
    (29, 1),
    (29, 4),
    (29, 14),
    (30, 1),
    (30, 4),
    (30, 14),
    (31, 1),
    (31, 4),
    (31, 14);
"""

INSERT_REVIEWERS_DATA = """
INSERT INTO reviewers (
    username,
    first_name,
    last_name,
    email,
    fave_genre_id,
    fave_book_id
)
VALUES 
    ('Zannadudu', 'Zan', 'Nadudu', 'zan@gmail.com', 9, 24),
    ('Aleeeece', 'Alice', 'Aforethought', 'alice@thought.com', 12, 5),
    ('JJ of Jay', 'John', 'Jefferies', 'john@gmail.com', 13, 6),
    ('Dan T Man', 'Daniel', 'Copestake', 'dan@hotmail.com', 6, 15);
"""

INSERT_REVIEWS_DATA = """
INSERT INTO reviews (
    book_id,
    review_title,
    review_body,
    rating,
    reviewer_id
)
VALUES
    (7, 'Hard going', 'No doubt this is a classic for a reason, but this was one of the hardest books to read. I couldn''t finish it; it was so bleak. Brilliantly written, but too close to the kuckle and made me very uncomfortable.', 3, 1),
    (1, 'Aliens love this', 'Great book as a Martian I found this very humorous. Nano Nano 🖖🏻', 5, 3),
    (11, 'Just wonderful (sigh)', 'Jane Austen wrote one of the most famous opening lines in English Literature. The dialogue and writing are like the delicate keys on a piano or Earl Grey being being poured into a china cup. Light delicious and fragrant. Lizzy is an intelligent, inspirational and engaging character, who doesn''t bow down to the social expectations of the time. This novel certainly deserves its place in the Top 10 of the BBC Big Read.', 5, 2),
    (7, 'Bought for my son', 'Bought this for my son so can''t review it properly although he said it was brilliant', 5, 4),
    (7, 'Fantastic read! Loved it.', 'One of the best books I have read in a while. I don''t usually like fiction, but this is something else. Fantastic read!', 5, 3),
    (1, 'Hilarious and Entertaining', 'One of the best books I''ve ever read, both sci-fi and comedy. It''s just so witty, clever, and amazing at subverting expectations in all the best ways. It''s honestly hard to put down. While the plot is simple, that doesn''t hinder the story to deliver a shockingly well developed galaxy and alien races. Highly recommend for anyone looking for a laugh.', 5, 1),
    (7, 'English', 'As an English literature student I required this book for my studies, it is a good copy of the book, easy to analyse', 4, 2),
    (11, 'I hate romance', 'Had to read this for school. It was awful and I never want to read anything like it again', 1, 3),
    (1, 'It''s decent but not the absolute best', null, 4, 4),
    (3, 'Happy birthday Peter Rabbit', '120 years since the first publication of the Tale of Peter Rabbit. A must for Beatrix Potter fans, a beautiful collectors book. Especially lovely as a gift for a new baby born this year or a child''s birthday - or adult birthday if a fan like me - Who doesn''t love Peter Rabbit ? 🐇', 5, 2);
"""
