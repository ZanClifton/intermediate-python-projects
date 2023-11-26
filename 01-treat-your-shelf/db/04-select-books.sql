\c treat_your_shelf;

\echo '\n----- the books we have in stock -----'

SELECT * FROM books WHERE quantity_in_stock > 0;

\echo '----- the non-fiction books -----'

SELECT * FROM books WHERE is_fiction = false;

\echo '----- the books released in the 1900s -----'

SELECT * FROM books WHERE release_date BETWEEN '1900-01-01' AND '1999-12-31';

\echo '----- the books with "the" in the title -----'

SELECT * FROM books WHERE title LIKE '% the %';

\echo '----- all of the books sorted in alphabetical order -----'

SELECT * FROM books ORDER BY title;

\echo '----- the most expensive book -----'

SELECT * FROM books ORDER BY price_in_pence DESC LIMIT 1;