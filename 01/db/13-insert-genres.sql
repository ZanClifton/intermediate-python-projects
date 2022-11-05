\c treat_your_shelf;

INSERT INTO genres (genre)
VALUES 
    ('adventure'),
    ('children''s'),
    ('classics'),
    ('comedy'),
    ('dystopian'),
    ('fantasy'),
    ('non-fiction'),
    ('romance'),
    ('science'),
    ('science-fiction')
;


\echo '\n----- all genres -----'
SELECT * FROM genres;