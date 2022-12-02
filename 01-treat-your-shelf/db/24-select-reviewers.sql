\c treat_your_shelf;

\echo '----- all reviewers -----'

SELECT * FROM reviewers;

\echo '----- all reviewers usernames, favourite genres, books and those books authors -----'

SELECT reviewers.username, genres.genre AS fave_genre, books.title AS fave_book, authors.author_name AS author_of_fave_book FROM reviewers
JOIN genres ON genres.id = reviewers.fave_genre_id
JOIN books ON books.id = reviewers.fave_book_id
JOIN authors ON authors.id = books.author_id; 