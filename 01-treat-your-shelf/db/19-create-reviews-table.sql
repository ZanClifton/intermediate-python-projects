\c treat_your_shelf;

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    review_title TEXT,
    review_body TEXT,
    rating INTEGER NOT NULL
);