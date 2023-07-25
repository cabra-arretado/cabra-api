-- Just an example right now
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO users (email, password) VALUES ('johndoe@example.com', "password123");
INSERT INTO users (email, password) VALUES ('janedoe@example.com', "password123");
