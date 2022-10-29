\c treat_your_shelf;

\echo '\n----- titles and authors sorted by author ----'

SELECT author_name, title FROM books
LEFT JOIN authors
ON books.author_id = authors.id
ORDER BY author_name;

-- SELECT author_name, title FROM authors
-- FULL OUTER JOIN books
-- ON books.author_id = authors.id
-- WHERE books.author_id = null
-- ORDER BY author_name;

\echo '\n----- authors without books in stock -----'

SELECT author_name AS authors_without_books_in_stock FROM authors
LEFT JOIN books
ON books.author_id = authors.id
WHERE books.author_id IS NULL;