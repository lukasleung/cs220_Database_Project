--  cid comment id
--  pid post id
--  uid user id
--  pos like

--  region ID 1, gives you "San Francisco"
CREATE TABLE IF NOT EXISTS  regions(
	rid INT AUTO_INCREMENT, --  region
	location varchar(20) NOT NULL, 
	PRIMARY KEY (rid),
	UNIQUE(location)
);

CREATE TABLE IF NOT EXISTS  topics(
	tid INT AUTO_INCREMENT, --  regions
	topic varchar(20) NOT NULL, 
	PRIMARY KEY (tid),
	UNIQUE(topic)
);

CREATE TABLE IF NOT EXISTS  users(
	uid INT AUTO_INCREMENT, -- user
	rid INT NOT NULL, -- regions of user
	pos INT DEFAULT 0, -- needs a trigger to update
	neg INT DEFAULT 0, -- needs a trigger to update
	PRIMARY KEY (uid),
	FOREIGN KEY (rid) REFERENCES regions(rid)
);

CREATE TABLE IF NOT EXISTS  posts(
	pid INT AUTO_INCREMENT, -- post
	uid INT NOT NULL, -- user of post
	content varchar (140) NOT NULL, -- OC
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- timestamp
	rid INT NOT NULL, -- regions of the post
	comments INT DEFAULT 0, -- needs a trigger to update, number of comments on a post
	pos INT DEFAULT 0,
	neg INT DEFAULT 0,
	PRIMARY KEY (pid),
	FOREIGN KEY (rid) REFERENCES regions(rid),
	FOREIGN KEY (uid) REFERENCES users(uid)
);
--  takes user regions


CREATE TABLE IF NOT EXISTS  comments(
	cid INT AUTO_INCREMENT, -- comment
	pid INT NOT NULL, -- post for which there is a comment
	uid INT NOT NULL, --  user who commented
	content varchar (140) NOT NULL, -- comment content
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- timestamp of comment
	pos INT DEFAULT 0,
	neg INT DEFAULT 0,
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


--  choose view by regions

--  organize by most recent 
--  organize by most pos
--  organize by most neg
--  organize by oldest time
--  organize by most commentsp


-- -------------------------------------------------------------------------(Add a Comment)

CREATE TRIGGER comment_add AFTER INSERT ON comments
FOR EACH ROW
UPDATE posts
SET posts.comments = posts.comments + 1
WHERE posts.pid = NEW.pid;

-- -------------------------------------------------------------------------( (Dis)Like a Comment)

delimiter //
CREATE TRIGGER update_comments_likes AFTER UPDATE ON comments_likes
FOR EACH ROW BEGIN
IF NEW.pos = 1 THEN
	UPDATE users
	SET users.pos = users.pos + 1, users.neg = users.neg - 1
	WHERE users.uid = NEW.ouid;
	
	UPDATE comments
	SET comments.pos = comments.pos + 1, comments.neg = comments.neg - 1
	WHERE comments.cid = NEW.cid;
ELSE
	UPDATE users
	SET users.neg = users.neg + 1, users.pos = users.pos -1
	WHERE users.uid = NEW.ouid;
	
	UPDATE comments
	SET comments.neg = comments.neg + 1, comments.pos = comments.pos -1
	WHERE comments.cid = NEW.cid;
END IF;
END;//
delimiter ;


delimiter //
CREATE TRIGGER comment_feedback AFTER INSERT ON comments_likes
FOR EACH ROW
BEGIN
IF NEW.pos = 1 THEN
	UPDATE users
	SET users.pos = users.pos + 1
	WHERE users.uid = NEW.ouid;
	
	UPDATE comments
	SET comments.pos = comments.pos + 1
	WHERE comments.cid = NEW.cid;
ELSE
	UPDATE users
	SET users.neg = users.neg + 1
	WHERE users.uid = NEW.ouid;
	
	UPDATE comments
	SET comments.neg = comments.neg + 1
	WHERE comments.cid = NEW.cid;
END IF;
END;//
delimiter ;


-- -------------------------------------------------------------------------( (Dis)Like a Post)

delimiter //
CREATE TRIGGER update_posts_likes AFTER UPDATE ON posts_likes
 FOR EACH ROW BEGIN
IF NEW.pos = 1 THEN
	UPDATE users
	SET users.pos = users.pos + 1, users.neg = users.neg - 1
	WHERE users.uid = NEW.ouid;
	
	UPDATE posts
	SET posts.pos = posts.pos + 1, posts.neg = posts.neg - 1
	WHERE posts.pid = NEW.pid;
ELSE
	UPDATE users
	SET users.neg = users.neg + 1, users.pos = users.pos -1
	WHERE users.uid = NEW.ouid;
	
	UPDATE posts
	SET posts.neg = posts.neg + 1, posts.pos = posts.pos -1
	WHERE posts.pid = NEW.pid;
END IF;
END;//
delimiter ;


delimiter //
CREATE TRIGGER post_feedback AFTER INSERT ON posts_likes
FOR EACH ROW
BEGIN
IF NEW.pos = 1 THEN
	UPDATE users
	SET users.pos = users.pos + 1
	WHERE users.uid = NEW.ouid;
	
	UPDATE posts
	SET posts.pos = posts.pos + 1
	WHERE posts.pid = NEW.pid;
	
ELSE
	UPDATE users
	SET users.neg = users.neg + 1
	WHERE users.uid = NEW.ouid;
	
		UPDATE posts
	SET posts.neg = posts.neg + 1
	WHERE posts.pid = NEW.pid;
END IF;
END;//
delimiter ;

INSERT INTO regions (rid, location)
VALUES
	(2, 'Outside Your Window'),
	(3, 'Over There'),
	(1, 'Under Where?');


INSERT INTO topics (tid, topic)
VALUES
	(2, 'Brandon\'s Basement'),
	(3, 'Coffee'),
	(1, 'Food');

-- uid, pos and neg are optional and have default values
-- INSERT INTO users (rid)
-- VALUES
-- 	(1),
-- 	(1),
-- 	(2),
-- 	(2),
-- 	(3),
-- 	(3);
INSERT INTO users (uid, rid, pos, neg)
VALUES
	(1, 1, 0, 0),
	(2, 1, 0, 0),
	(3, 2, 0, 0),
	(4, 2, 0, 0),
	(5, 3, 0, 0),
	(6, 3, 0, 0);

-- pid, ts, comments, pos and neg are optional and have default values
-- INSERT INTO posts (uid, content, rid)
-- VALUES
-- 	(1, 'You eated my cookies', 1),
-- 	(2, 'Caffine is my hero', 2);
INSERT INTO posts (pid, uid, content, ts, rid, comments, pos, neg)
VALUES
	(1, 1, 'You eated my cookies', '2015-04-23 14:03:12', 1, 0,0,0),
	(2, 2, 'Caffine is my hero', '2015-04-23 14:03:49', 2, 0,0,0);

-- ts is optional and has a default value
-- INSERT INTO posts_likes (uid, pid, pos, ouid)
-- VALUES
-- 	(1, 1, 1, 1),
-- 	(2, 1, 0, 1),
-- 	(4, 2, 1, 3);
INSERT INTO posts_likes (uid, pid, pos, ouid, ts)
VALUES
	(1, 1, 1, 1, '2015-04-23 14:04:53'),
	(2, 1, 0, 1, '2015-04-23 14:05:21'),
	(4, 2, 1, 3, '2015-04-23 14:07:25');

-- cid, ts, pos and neg are optional and have default values
-- INSERT INTO comments (pid, uid, content)
-- VALUES
-- 	(1, 2, 'Those were my cookies.'),
-- 	(2, 4, 'My house smells like coffee');
INSERT INTO comments (cid, pid, uid, content, ts, pos, neg)
VALUES
	(1, 1, 2, 'Those were my cookies.', '2015-04-23 14:08:25',0,0),
	(2, 2, 4, 'My house smells like coffee', '2015-04-23 14:09:11',0,0);

-- ts is optional and has a default value
-- INSERT INTO comments_likes (cid, uid, pos, ouid)
-- VALUES
-- 	(1, 2, 1, 1),
-- 	(2, 3, 1, 4);
 
INSERT INTO comments_likes (cid, uid, pos, ouid, ts)
VALUES
	(1, 2, 1, 1, '2015-04-23 14:09:44'),
	(2, 3, 1, 4, '2015-04-23 14:09:56');
