--  cid comment id
--  pid post id
--  uid user id
--  pos like

--  region ID 1, gives you "San Francisco"
CREATE TABLE IF NOT EXISTS  region(
	rid INT AUTO_INCREMENT, --  region
	location varchar(20) NOT NULL, 
	PRIMARY KEY (rid),
	UNIQUE(location)
);

CREATE TABLE IF NOT EXISTS  topics(
	tid INT AUTO_INCREMENT, --  region
	topic varchar(20) NOT NULL, 
	PRIMARY KEY (tid),
	UNIQUE(topic)
);

CREATE TABLE IF NOT EXISTS  users(
	uid INT AUTO_INCREMENT, -- user
	rid INT NOT NULL, -- region of user
	pos INT DEFAULT 0, -- needs a trigger to update
	neg INT DEFAULT 0, -- needs a trigger to update
	PRIMARY KEY (uid),
	FOREIGN KEY (rid) REFERENCES region(rid)
);

CREATE TABLE IF NOT EXISTS  posts(
	pid INT AUTO_INCREMENT, -- post
	uid INT NOT NULL, -- user of post
	content varchar (140) NOT NULL, -- OC
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- timestamp
	rid INT NOT NULL, -- region of the post
	comments INT DEFAULT 0, -- needs a trigger to update, number of comments on a post
	PRIMARY KEY (pid),
	FOREIGN KEY (rid) REFERENCES region(rid),
	FOREIGN KEY (uid) REFERENCES users(uid)
);
--  takes user region


CREATE TABLE IF NOT EXISTS  comments(
	cid INT AUTO_INCREMENT, -- comment
	pid INT NOT NULL, -- post for which there is a comment
	uid INT NOT NULL, --  user who commented
	content varchar (140) NOT NULL, -- comment content
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- timestamp of comment
	PRIMARY KEY (cid),
	FOREIGN KEY (uid) REFERENCES users(uid),
	FOREIGN KEY (pid) REFERENCES posts(pid)
--  	PRIMARY KEY (pid, cid)
);
--  CID counts the number of comments on a post

-- insertions changes above post, users pos/neg
CREATE TABLE IF NOT EXISTS  posts_likes(
	uid INT NOT NULL, -- who liked the post
	pid INT NOT NULL, -- the post in question
	pos BOOLEAN NOT NULL, --  like or dislike of post
	ouid INT NOT NULL, -- user who created the post
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (uid, pid),
	FOREIGN KEY (pid) REFERENCES posts(pid),
	FOREIGN KEY (uid) REFERENCES users(uid),
	FOREIGN KEY (ouid) REFERENCES users(uid)
);

-- Insertions->update posts, comments, users pos/neg
CREATE TABLE IF NOT EXISTS  comments_likes(
	cid INT NOT NULL, -- the comment in question
	uid INT NOT NULL, -- who liked the comment
	pos BOOLEAN NOT NULL, -- like or dislike of comment
	ouid INT NOT NULL, -- user who created the post
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (uid, cid),
	FOREIGN KEY (cid) REFERENCES comments(cid),
	FOREIGN KEY (uid) REFERENCES users(uid),
	FOREIGN KEY (ouid) REFERENCES users(uid)
);


--  choose view by region

--  organize by most recent 
--  organize by most pos
--  organize by most neg
--  organize by oldest time
--  organize by most commentsp
