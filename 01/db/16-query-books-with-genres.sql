\c treat_your_shelf;

\echo '\n----- all books with genres -----'

SELECT
  books.title,
  genres.genre
FROM books_genres
JOIN books ON books.id = books_genres.book_id
JOIN genres ON genres.id = books_genres.genre_id;

\echo '\n----- all genres for a single book -----'

SELECT
  books.title,
  genres.genre
FROM books_genres
JOIN books ON books.id = books_genres.book_id
JOIN genres ON genres.id = books_genres.genre_id
WHERE books.id = 2;

\echo '\n----- all books for a single genre -----'

SELECT
  genres.genre,
  books.title
FROM books_genres
JOIN books ON books.id = books_genres.book_id
JOIN genres ON genres.id = books_genres.genre_id
WHERE genres.id = 14;

