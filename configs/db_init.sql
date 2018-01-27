CREATE USER madtoss WITH PASSWORD 'madpass';

CREATE TABLE players (
	id SERIAL PRIMARY KEY NOT NULL,
	username VARCHAR NOT NULL UNIQUE,
	password VARCHAR,
	balance MONEY,
	country VARCHAR,
	registered_date TIMESTAMP,
	last_played TIMESTAMP,
	wagered DECIMAL,
	profit DECIMAL,
	number_of_chat_messages INT,
	number_of_bets INT,
	number_of_bets_won INT
);

CREATE TABLE bets 
(
	id SERIAL PRIMARY KEY NOT NULL,
	player_id INT NOT NULL REFERENCES players(id),
	bet_amount MONEY,
	date TIMESTAMP,
	house_won BIT,
	chance DECIMAL
);

CREATE TABLE statuses (
	id INT PRIMARY KEY,
	definition VARCHAR
);

CREATE TABLE player_deposits (
    id SERIAL PRIMARY KEY NOT NULL,
    player_id INT NOT NULL REFERENCES players(id),
    deposit_amount MONEY,
    status_id INT REFERENCES statuses(id),
    date TIMESTAMP
);

CREATE TABLE player_withdrawals (
    id SERIAL PRIMARY KEY NOT NULL,
    player_id INT NOT NULL REFERENCES players(id),
    withrawal_amount MONEY,
    status_id INT REFERENCES statuses(id),
    date TIMESTAMP
);

CREATE TABLE player_messages (
	id SERIAL PRIMARY KEY NOT NULL,
	sender_id INT REFERENCES players(id),
	receiver_id INT REFERENCES players(id),
	content VARCHAR,
	date TIMESTAMP
);
