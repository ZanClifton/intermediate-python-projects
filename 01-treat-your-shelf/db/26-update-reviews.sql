\c treat_your_shelf;

UPDATE reviews
SET reviewer_id=CASE
    WHEN id=1 THEN 1
    WHEN id=2 THEN 3
    WHEN id=3 THEN 2
    WHEN id=4 THEN 4
    WHEN id=5 THEN 3
    WHEN id=6 THEN 1
    WHEN id=7 THEN 2
    WHEN id=8 THEN 3
    WHEN id=9 THEN 4
    WHEN id=10 THEN 2
END;

ALTER TABLE reviews
ADD CONSTRAINT reviews_reviewer_id_fk
FOREIGN KEY (reviewer_id)
REFERENCES reviewers(id);
