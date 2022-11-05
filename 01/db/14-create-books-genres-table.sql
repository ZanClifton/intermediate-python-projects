\c treat_your_shelf;

CREATE TABLE books_genres (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    genre_id INTEGER REFERENCES genres(id)
);

SELECT * FROM books_genres;