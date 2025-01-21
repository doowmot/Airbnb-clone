DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    listing_id INTEGER,
    name VARCHAR(255),
    description VARCHAR(255),
    price INTEGER
);

INSERT INTO spaces (listing_id, name, description, price) VALUES (1, 'The Oasis', 'Enjoy views of the beach', 100);
INSERT INTO spaces (listing_id, name, description, price) VALUES (1, 'Riverbend Cabin', 'Explore the woods', 200);
INSERT INTO spaces (listing_id, name, description, price) VALUES (2, 'Skycabin', 'Great views of the nightsky', 150);
INSERT INTO spaces (listing_id, name, description, price) VALUES (2, 'The Glen', 'Amazing town to explore', 200);
INSERT INTO spaces (listing_id, name, description, price) VALUES (3, 'Aurora', 'Nightlife at your fingertip', 100);