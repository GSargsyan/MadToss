CREATE DATABASE madtoss;

CREATE TABLE players (
	id int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	username varchar(255) NOT NULL UNIQUE,
	password blob,
	amount decimal(15, 11),
	country varchar(255),
	registered_date date,
	last_played date,
	num_of_iterations int(11),
	salt blob,
	wagered decimal(15, 11),
	profit decimal(15, 11),
	chat_messages int(11),
	number_of_bets int(11),
	number_of_bets_lost int(11)
);
