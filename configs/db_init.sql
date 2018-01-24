CREATE DATABASE madtoss;

CREATE TABLE players (
	id SERIAL PRIMARY KEY NOT NULL,
	username VARCHAR NOT NULL UNIQUE,
	password VARCHAR,
	balance MONEY,
	country varchar,
	registered_date DATE,
	last_played DATE,
	wagered DECIMAL,
	profit DECIMAL,
	chat_messages INT,
	number_of_bets INT,
	number_of_bets_won INT
);

CREATE TABLE bets 
(
	id SERIAL PRIMARY KEY NOT NULL,
	player_id INT NOT NULL,
	amount DECIMAL,
	date DATETIME,
	house_won BIT,
	chance DECIMAL,
	FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE player_deposits (
	id SERIAL PRIMARY KEY,
	player_id INT,
);

CREATE TABLE player_deposits (
);
