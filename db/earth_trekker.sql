DROP TABLE cities;
DROP TABLE countries;


CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN,
  country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);




