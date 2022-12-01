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

\echo '\n----- the most favourable review for Pride and Prejudice -----'

SELECT 
    books.title, reviews.rating, reviews.review_title, reviews.rating, reviews.review_body
FROM reviews
JOIN books ON books.id = reviews.book_id
WHERE book_id = 11 AND reviews.rating = (SELECT MAX(reviews.rating) from reviews)
GROUP BY books.title, reviews.rating, reviews.review_title, reviews.review_body;

\echo '\n----- the least favourable review for Pride and Prejudice -----'

SELECT 
    books.title, reviews.rating, reviews.review_title, reviews.review_body
FROM reviews
JOIN books ON books.id = reviews.book_id
WHERE book_id = 11 AND reviews.rating = (SELECT MIN(reviews.rating) from reviews)
GROUP BY books.title, reviews.rating, reviews.review_title, reviews.review_body;

\echo '\n----- not-deleted books with ratings 4 and over -----'

SELECT books.id, books.title, AVG(reviews.rating) AS average_rating
FROM reviews
JOIN books ON books.id = reviews.book_id
GROUP BY books.id
HAVING AVG(reviews.rating) >= 4;

\echo '\n----- not-deleted books with ratings over the average rating -----'

SELECT books.id, books.title, AVG(reviews.rating) AS average_rating
FROM reviews
JOIN books ON books.id = reviews.book_id
GROUP BY books.id
HAVING AVG(reviews.rating) > (SELECT AVG(reviews.rating) FROM reviews);

