\c treat_your_shelf;

\echo '----- number of titles stocked for each author -----'

SELECT authors.author_name, COUNT(books.title) AS no_of_titles_stocked
FROM books
RIGHT JOIN authors ON authors.id = books.author_id
GROUP BY authors.author_name;

\echo '----- number of titles by douglas adams stocked -----'

SELECT authors.author_name, COUNT(books.title) AS no_of_titles_stocked
FROM books
JOIN authors ON authors.id = books.author_id
WHERE authors.id = 3
GROUP BY authors.author_name;

\echo '----- total number of books stocked for each author -----'

SELECT authors.author_name, SUM(books.quantity_in_stock) AS total_no_of_books_in_stock
FROM books
RIGHT JOIN authors ON authors.id = books.author_id
GROUP BY authors.author_name;

\echo '----- average price of books in all genres -----'

SELECT
  genres.genre,
  ROUND(AVG(books.price_in_pence)) AS avg_price_in_pence
FROM books_genres
JOIN books ON books.id = books_genres.book_id
JOIN genres ON genres.id = books_genres.genre_id
GROUP BY genres.genre;