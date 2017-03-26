CREATE TABLE IF NOT EXISTS transaction (
  id serial PRIMARY KEY,
  memo varchar(255) NOT NULL CHECK (memo <> ''),
  amount money NOT NULL,
  category varchar(255) NOT NULL CHECK (category <> ''),
  timestamp timestamp DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS ACCOUNT (
  id serial PRIMARY KEY,
  name varchar(255) NOT NULL CHECK (name <> ''),
  amount money NOT NULL
);
