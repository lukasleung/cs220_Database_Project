-- cid comment id
-- pid post id
-- uid user id
-- pos like

CREATE TABLE region(
	rid INT AUTO_INCREMENT,
	location varchar(20) NOT NULL,
	PRIMARY KEY (rid),
	UNIQUE(location)
)

CREATE TABLE users(
	uid INT AUTO_INCREMENT,
	rid INT NOT NULL,
	pos INT DEFAULT 0,
	neg INT DEFAULT 0,
	PRIMARY KEY (uid),
	FOREIGN KEY (rid) REFERENCES region(rid)
)

CREATE TABLE posts(
	pid INT AUTO_INCREMENT,
	uid INT NOT NULL,
	content varchar (140) NOT NULL,
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	rid INT NOT NULL,
-- 	varchar(20) NOT NULL, 
	comments INT DEFAULT 0,
	pos INT DEFAULT 0,
	neg INT DEFAULT 0,
	PRIMARY KEY (pid),
	FOREIGN KEY (rid) REFERENCES region(rid)
)
-- takes user region


CREATE TABLE comments(
	cid INT AUTO_INCREMENT,
	pid INT NOT NULL,
	uid INT NOT NULL,
	content varchar (140) NOT NULL,
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	pos INT DEFAULT 0,
	neg INT DEFAULT 0,
	PRIMARY KEY (cid)
-- 	PRIMARY KEY (pid, cid)
)
-- CID counts the number of comments on a post

CREATE TABLE posts_likes(
	uid INT NOT NULL,
	pid INT NOT NULL,
	pos BOOLEAN NOT NULL,
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (uid, pid),
	FOREIGN KEY (pid) REFERENCES posts(pid),
	FOREIGN KEY (uid) REFERENCES users(uid)
)

CREATE TABLE comments_likes(
	uid INT NOT NULL,
	pid INT NOT NULL,
	pos BOOLEAN NOT NULL,
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (uid, pid),
	FOREIGN KEY (pid) REFERENCES posts(pid),
	FOREIGN KEY (uid) REFERENCES users(uid)
)


-- choose view by region

-- organize by most recent 
-- organize by most pos
-- organize by most neg
-- organize by oldest time
-- organize by most commentsp