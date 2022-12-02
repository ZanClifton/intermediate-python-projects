\c treat_your_shelf;

\echo '----- by author name select all reviews -----'

SELECT authors.author_name, books.title, reviewers.username, reviews.rating, reviews.review_title, reviews.review_body FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
JOIN books ON books.id = reviews.book_id
JOIN authors ON authors.id = books.author_id
ORDER BY authors.author_name, books.title ASC;

\echo '----- select all reviews by a single reviewer -----\n\n----- Zannadudu'


SELECT reviewers.username, authors.author_name, books.title, reviews.rating, reviews.review_title, reviews.review_body FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
JOIN books ON books.id = reviews.book_id
JOIN authors ON authors.id = books.author_id
WHERE reviewers.id = 1
ORDER BY authors.author_name, books.title ASC;

\echo '----- Aleeeece'

SELECT reviewers.username, authors.author_name, books.title, reviews.rating, reviews.review_title, reviews.review_body FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
JOIN books ON books.id = reviews.book_id
JOIN authors ON authors.id = books.author_id
WHERE reviewers.id = 2
ORDER BY authors.author_name, books.title ASC;

\echo '----- JJ of Jay'

SELECT reviewers.username, authors.author_name, books.title, reviews.rating, reviews.review_title, reviews.review_body FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
JOIN books ON books.id = reviews.book_id
JOIN authors ON authors.id = books.author_id
WHERE reviewers.id = 3
ORDER BY authors.author_name, books.title ASC;

\echo '----- Dan T Man'

SELECT reviewers.username, authors.author_name, books.title, reviews.rating, reviews.review_title, reviews.review_body FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
JOIN books ON books.id = reviews.book_id
JOIN authors ON authors.id = books.author_id
WHERE reviewers.id = 4
ORDER BY authors.author_name, books.title ASC;

\echo '----- average ratings each reviewer has given (deleted books included) -----'

SELECT reviewers.username, ROUND(AVG(reviews.rating), 2) AS average_rating FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
GROUP BY reviewers.username;

\echo '----- average ratings each reviewer has given (deleted books excluded) -----'

SELECT reviewers.username, ROUND(AVG(reviews.rating), 2) AS average_rating FROM reviews
JOIN reviewers ON reviewers.id = reviews.reviewer_id
JOIN books ON books.id = reviews.book_id
WHERE books.title IS NOT NULL
GROUP BY reviewers.username;

\echo '----- books not reviewed by a user -----'

SELECT DISTINCT books.title AS not_reviewed_by_aleeeece
FROM books
WHERE NOT EXISTS (
    SELECT * FROM reviews
    WHERE reviews.book_id = books.id
    AND reviews.reviewer_id = 2
);

SELECT DISTINCT books.title AS not_reviewed_by_dan_t_man
FROM books
WHERE NOT EXISTS (
    SELECT * FROM reviews
    WHERE reviews.book_id = books.id
    AND reviews.reviewer_id = 4
);