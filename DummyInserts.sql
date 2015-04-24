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
