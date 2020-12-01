DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vetenarians;

CREATE TABLE vetenarians (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    animal_type VARCHAR(255),
    contact_details VARCHAR(255),
    notes TEXT,
    vetenarian_id INT REFERENCES vetenarians(id)
);

