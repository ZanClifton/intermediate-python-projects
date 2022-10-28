\c treat_your_shelf;

ALTER TABLE books
ADD author_id INT;

\echo "\n----- updated books table -----"

SELECT * FROM books;