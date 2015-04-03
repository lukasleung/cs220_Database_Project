CREATE TABLE user(
	uid INT AUTO_INCREMENT PRIMARY KEY,
	first_name varchar(255),
	last_name varchar (255),
	points INT DEFAULT 0,
	email varchar(20) NOT NULL UNIQUE,
	username varchar(20) NOT NULL UNIQUE,
	password varchar (20) NOT NULL
)

CREATE TABLE post
	pid INT AUTO_INCREMENT PRIMARY KEY,
	uid INT NOT NULL,
	content varchar (255) NOT NULL
	time timestamp DEFAULT CURRENT_TIMESTAMP
	
)

-- CREATE TABLE comment(
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
-- 	first_name varchar(255)
-- 	last_name varchar (255)
-- 	points INT DEFAULT 0
-- 	email varchar(20) NOT NULL UNIQUE
-- 	username varchar(20) NOT NULL UNIQUE
-- 	password varchar (20) NOT NULL
-- )