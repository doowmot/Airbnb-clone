-- Drop sequences and tables if they exist
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS users;

DROP SEQUENCE IF EXISTS booking_id_seq;
DROP SEQUENCE IF EXISTS date_id_seq;
DROP SEQUENCE IF EXISTS space_id_seq;
DROP SEQUENCE IF EXISTS listing_id_seq;
DROP SEQUENCE IF EXISTS user_id_seq;

-- Recreate sequences
CREATE SEQUENCE IF NOT EXISTS user_id_seq;
CREATE SEQUENCE IF NOT EXISTS listing_id_seq;
CREATE SEQUENCE IF NOT EXISTS space_id_seq;
CREATE SEQUENCE IF NOT EXISTS date_id_seq;
CREATE SEQUENCE IF NOT EXISTS booking_id_seq;

-- Create users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_email VARCHAR(255),
    user_password VARCHAR(255)
);

-- Create listings table
CREATE TABLE listings (
    listing_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE
);

-- Create spaces table
CREATE TABLE spaces (
    space_id SERIAL PRIMARY KEY,
    space_name VARCHAR(255),
    space_description VARCHAR(255),
    space_price_per_night INTEGER,
    listing_id INTEGER REFERENCES listings (listing_id) ON DELETE CASCADE
);

-- Create dates table
CREATE TABLE dates (
    date_id SERIAL PRIMARY KEY,
    date DATE, -- Use DATE type for dates
    available BOOLEAN,
    space_id INTEGER REFERENCES spaces (space_id) ON DELETE CASCADE
);

-- Create bookings table
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    booking_status BOOLEAN,
    space_id INTEGER REFERENCES spaces (space_id) ON DELETE CASCADE,
    date_id INTEGER REFERENCES dates (date_id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users (user_id) ON DELETE CASCADE
);





-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (user_email, user_password) VALUES ('test@gmail.com', 'test_password');
INSERT INTO listings (user_id) VALUES (1);

INSERT INTO spaces (space_name, space_description, space_price_per_night, listing_id) 
VALUES ('test_space_name', 'test_space_description', 100, 1);

INSERT INTO dates (date, available, space_id)
VALUES ('2025-01-01', TRUE, 1);

INSERT INTO bookings (booking_status, space_id, date_id, user_id)
VALUES (TRUE, 1, 1, 1);
