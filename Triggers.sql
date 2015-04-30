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
