\c treat_your_shelf;

\echo '\n----- deleted books due to lack of stock -----'

DELETE FROM books WHERE quantity_in_stock = 0 RETURNING *;