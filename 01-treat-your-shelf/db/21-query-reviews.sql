\c treat_your_shelf;

\echo '\n----- all available reviews -----'

SELECT * FROM reviews;

\echo '\n----- all reviews of The Handmaid'' Tale -----'

SELECT books.title, reviews.rating, reviews.review_title, reviews.review_body FROM reviews
JOIN books ON books.id = reviews.book_id
WHERE books.title = 'The Handmaid''s Tale';

\echo '\n----- the average rating of each book -----'

SELECT book_id, ROUND(AVG(rating), 2) AS average_rating 
FROM reviews
GROUP BY book_id;

\echo '\n----- the average rating of The Handmaid''s Tale -----'

SELECT books.title, ROUND(AVG(reviews.rating), 2) AS average_rating 
FROM reviews
JOIN books ON books.id = reviews.book_id
WHERE book_id = 7
GROUP BY books.title;

