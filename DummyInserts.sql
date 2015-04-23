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


INSERT INTO users (uid, rid, pos, neg)
VALUES
	(1, 1, 0, 0),
	(2, 1, 0, 0),
	(3, 2, 0, 0),
	(4, 2, 0, 0),
	(5, 3, 0, 0),
	(6, 3, 0, 0);

INSERT INTO posts (pid, uid, content, ts, rid, comments)
VALUES
	(1, 1, 'You eated my cookies', '2015-04-23 14:03:12', 1, 0),
	(2, 2, 'Caffine is my hero', '2015-04-23 14:03:49', 2, 0);


INSERT INTO posts_likes (uid, pid, pos, ouid, ts)
VALUES
	(1, 1, 1, 1, '2015-04-23 14:04:53'),
	(2, 1, 0, 1, '2015-04-23 14:05:21'),
	(4, 2, 1, 3, '2015-04-23 14:07:25');


INSERT INTO comments (cid, pid, uid, content, ts)
VALUES
	(1, 1, 2, 'Those were my cookies.', '2015-04-23 14:08:25'),
	(2, 2, 4, 'My house smells like coffee', '2015-04-23 14:09:11');


INSERT INTO comments_likes (cid, uid, pos, ouid, ts)
VALUES
	(1, 2, 1, 1, '2015-04-23 14:09:44'),
	(2, 3, 1, 4, '2015-04-23 14:09:56');
