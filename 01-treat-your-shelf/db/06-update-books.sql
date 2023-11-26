\c treat_your_shelf;

UPDATE books 
SET price_in_pence = price_in_pence * 0.9 
WHERE quantity_in_stock > 100;

\echo '\n----- books on sale due to excess stock -----'

SELECT * FROM books;