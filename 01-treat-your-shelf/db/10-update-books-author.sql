\c treat_your_shelf;

UPDATE books
SET author_id=CASE
    WHEN id=1 THEN 3
    WHEN id=3 THEN 2
    WHEN id=4 THEN 7
    WHEN id=5 THEN 14
    WHEN id=6 THEN 13
    WHEN id=7 THEN 15
    WHEN id=8 THEN 12
    WHEN id=11 THEN 14
    WHEN id=2 THEN 3
    WHEN id=12 THEN 9
    WHEN id=13 THEN 9 
    WHEN id=14 THEN 9
    WHEN id=15 THEN 9
    WHEN id=16 THEN 9 
    WHEN id=17 THEN 9
    WHEN id=18 THEN 9
    WHEN id=19 THEN 9 
    WHEN id=20 THEN 9 
    WHEN id=21 THEN 9
    WHEN id=22 THEN 9
    WHEN id=23 THEN 9
    WHEN id=24 THEN 9
    WHEN id=25 THEN 9
    WHEN id=26 THEN 3
    WHEN id=27 THEN 3
    WHEN id=28 THEN 3
    WHEN id=29 THEN 3
    WHEN id=30 THEN 3
    WHEN id=31 THEN 3
    WHEN id=32 THEN 3
END;

ALTER TABLE books
ADD CONSTRAINT books_author_id_fk 
FOREIGN KEY (author_id)
REFERENCES authors(id);

\echo '\n----- books with author_id -----'

SELECT * FROM books;