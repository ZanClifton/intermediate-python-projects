\c treat_your_shelf;

UPDATE books
SET author_id=CASE
    WHEN title='The Hitchhiker''s Guide to the Galaxy' THEN 3
    WHEN title='The Little Prince' THEN 2
    WHEN title='The Tale of Peter Rabbit' THEN 7
    WHEN title='Emma' THEN 14
    WHEN title='Nineteen Eighty-Four: A Novel' THEN 13
    WHEN title='The Handmaid''s Tale' THEN 15
    WHEN title='The War of the Worlds' THEN 12
    WHEN title='Pride and Prejudice' THEN 14
    WHEN title='The Restaurant at the End of the Universe' THEN 3
END;

\echo '\n----- books with author_id -----'

SELECT * FROM books;