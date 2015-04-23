-- -------------------------------------------------------------------------(Add a Comment)

CREATE TRIGGER comment_add AFTER INSERT ON comments
FOR EACH ROW
UPDATE posts
SET posts.comments = posts.comments + 1
WHERE posts.pid = NEW.pid;

-- -------------------------------------------------------------------------( (Dis)Like a Comment)
delimiter //
CREATE TRIGGER comment_feedback AFTER INSERT ON comments_likes
FOR EACH ROW 
IF NEW.pos = 1 THEN
	UPDATE users
	SET users.pos = users.pos + 1
	WHERE users.uid = NEW.ouid;
ELSE
	UPDATE users
	SET users.neg = users.neg + 1
	WHERE users.uid = NEW.ouid;
END IF;//
delimiter ;


-- -------------------------------------------------------------------------( (Dis)Like a Post)

delimiter //
CREATE TRIGGER `post_feedback` AFTER INSERT ON `posts_likes`
 FOR EACH ROW IF NEW.pos = 1 THEN
	UPDATE users
	SET users.pos = users.pos + 1
	WHERE users.uid = NEW.ouid;
ELSE
	UPDATE users
	SET users.neg = users.neg + 1
	WHERE users.uid = NEW.ouid;
END IF;//
delimiter ;
