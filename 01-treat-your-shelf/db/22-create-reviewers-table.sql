\c treat_your_shelf;

CREATE TABLE reviewers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    fave_genre_id INT,
    fave_book_id INT
);