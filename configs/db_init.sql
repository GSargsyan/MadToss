CREATE USER madtoss WITH PASSWORD 'madpass';
CREATE DATABASE madtoss;
GRANT ALL PRIVILEGES ON DATABASE madtoss TO madtoss;

-- TODO: keep both last_played and last_logged_in dates
-- TODO: keep also how much plays on average when logged
-- So that to know if chats or plays
CREATE TABLE players (
	id SERIAL PRIMARY KEY NOT NULL,
	username VARCHAR NOT NULL UNIQUE,
	password VARCHAR,
	balance NUMERIC(15, 12),
	country VARCHAR,
	registered_date TIMESTAMP,
	last_played TIMESTAMP,
	wagered NUMERIC(15, 12),
	profit NUMERIC(15, 12),
	status_id INT REFERENCES(player_statuses.id),
	number_of_chat_messages INT,
	number_of_bets INT,
	number_of_bets_won INT
);

CREATE TABLE coins (
	id SERIAL PRIMARY KEY NOT NULL,
	server_seed VARCHAR NOT NULL,
	server_seed_hash VARCHAR NOT NULL,
	client_seed VARCHAR NOT NULL,
	nonce INT NOT NULL
);

CREATE TYPE COIN_SIDE AS ENUM ('H', 'T');

CREATE TABLE bets 
(
	id SERIAL PRIMARY KEY NOT NULL,
	player_id INT NOT NULL REFERENCES players(id),
	coin_id INT REFERENCES coins(id) NOT NULL,
	amount NUMERIC(15, 12) NOT NULL,
	date TIMESTAMP,
	bet_on COIN_SIDE NOT NULL,
	outcome COIN_SIDE NOT NULL,
	chance NUMERIC(4, 2)
);

CREATE TABLE transaction_statuses (
	id SERIAL PRIMARY KEY NOT NULL,
	definition VARCHAR
);

CREATE TABLE player_statuses (
	id SERIAL PRIMARY KEY,
	definition VARCHAR
);

CREATE TABLE player_deposits (
    id SERIAL PRIMARY KEY NOT NULL,
    player_id INT NOT NULL REFERENCES players(id),
    deposit_amount NUMERIC(15, 12),
    status_id INT REFERENCES statuses(id),
    date TIMESTAMP
);

CREATE TABLE player_withdrawals (
    id SERIAL PRIMARY KEY NOT NULL,
    player_id INT NOT NULL REFERENCES players(id),
    withrawal_amount NUMERIC(15, 12),
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
