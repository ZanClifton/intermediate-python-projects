\c treat_your_shelf;

INSERT INTO genres (genre)
VALUES 
    ('adventure'),
    ('children''s'),
    ('classics'),
    ('comedy'),
    ('dystopian'),
    ('fantasy'),
    ('historical fiction'),
    ('horror'),
    ('mystery'),
    ('nonfiction'),
    ('paranormal'),
    ('romance'),
    ('science'),
    ('science fiction'),
    ('thriller'),
    ('young adult');


\echo '\n----- all genres -----'
SELECT * FROM genres;