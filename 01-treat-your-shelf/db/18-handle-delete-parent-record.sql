\c treat_your_shelf;

-- Modified file 14-create-books-genres-table.sql to
-- cascade on delete
-- I have had to modify the original table because
-- adding the constraint after the table creation has
-- a different effect on the cascade
-- By modifying the original create table query it
-- permits the book's deletion via the book table
-- By adding the modification subsequently, the book
-- must be deleted from the books_genres table

-- Modified file 10-update-books-table.sql to
-- cascade on delete

\echo '----- show the author, title and genres for "Mostly Harmless" -----'

SELECT authors.author_name, books.title, ARRAY_AGG(genres.genre) AS genres
FROM books_genres
JOIN books ON books.id = books_genres.book_id
JOIN genres ON genres.id = books_genres.genre_id
JOIN authors ON authors.id = books.author_id
WHERE author_id = 3 AND books.title = 'Mostly Harmless'
GROUP BY authors.author_name, books.title;
\echo '----- deletes "Mostly Harmless" from all tables -----'

DELETE FROM books WHERE id = 30;
\echo ' '

\echo '--- shows all books by Douglas Adams - "Mostly Harmless" has been deleted ----'

SELECT authors.author_name, books.title, ARRAY_AGG(genres.genre) AS genres 
FROM books_genres
JOIN books ON books.id = books_genres.book_id
JOIN genres ON genres.id = books_genres.genre_id
JOIN authors ON authors.id = books.author_id
WHERE author_id = 3
GROUP BY authors.author_name, books.title;

\echo '----- drops foreign key restraint on books table -----'

ALTER TABLE books
DROP CONSTRAINT books_author_id_fk;
\echo ' '
\echo '----- adds foreign key constraint back with on delete cascade added -----'

ALTER TABLE books 
ADD CONSTRAINT books_author_id_fk 
FOREIGN KEY (author_id)
REFERENCES authors(id)
ON DELETE CASCADE;
\echo ' '
\echo '----- deletes Douglas Adams and all his books -----'

DELETE FROM authors
WHERE id = 3;
\echo ' '
\echo '----- authors and their books - Douglas Adams and his books have been deleted -----'

SELECT authors.author_name, books.title FROM books
RIGHT JOIN authors ON authors.id = books.author_id
ORDER BY authors.author_name;
