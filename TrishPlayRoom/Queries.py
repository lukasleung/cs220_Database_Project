import MySQLdb as db

# global db connection for ease of coding
#filename = "university.db"
# conn = db.connect(filename)

############################################################
def dbCursor():
    conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
    cursor = conn.cursor()
    return conn, cursor
############################################################
def login_page():
    conn, cursor = dbCursor()
    sql = """SELECT uid, users.rid, location
            FROM users, regions
            WHERE users.rid=regions.rid
            ORDER BY users.uid"""
    params = ()
    cursor.execute(sql, )
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
############################################################
def add_user(rid):
    conn, cursor = dbCursor()
    sql = """INSERT INTO users (rid)
            VALUES
            ( %s );"""
    params = (rid, )
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
############################################################
def posts_region(rid, order_rule="recent"):
    conn, cursor = dbCursor()
    sql = """SELECT pid, content, comments, pos, neg
            FROM posts
            WHERE posts.rid= %s """
    if order_rule == "recent":
        sql+= " ORDER BY posts.ts DESC;"
    elif order_rule == "positive":
        sql+= " ORDER BY posts.pos DESC;"
    elif order_rule == "negative":
        sql+= " ORDER BY posts.neg DESC;"
    elif order_rule == "controversial": 
        sql+= " and posts.pos+posts.neg !=0 "
        sql+= " ORDER BY abs((1/16)-(power((pos/(pos+neg)),3)+ power((neg/(pos+neg)),3)));"
    elif order_rule == "comments":
        sql+= " ORDER BY posts.comments DESC;"
    elif order_rule == "interaction":
        sql+= " ORDER BY posts.pos+posts.neg+posts.comments DESC;"
    else:
        sql+= " ORDER BY posts.ts DESC;"
    params = (rid, )
    cursor.execute(sql, params)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
############################################################
def create_post(uid, content, rid):
    conn, cursor = dbCursor()
    sql = """INSERT INTO posts (uid, content, rid)
            VALUES
            ( %s ,  %s , %s );"""
    params = (uid, content, rid)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()

############################################################
def get_ouid_post(pid):
    conn, cursor = dbCursor()
    sql = """SELECT uid
            FROM posts
            WHERE posts.pid= %s """
    params = (pid, )
    cursor.execute(sql, params)
    ouid = cursor.fetchone()
    cursor.close()
    conn.close()
    return ouid

############################################################
def get_ouid_comment(cid):
    conn, cursor = dbCursor()
    sql = """SELECT uid
            FROM comments
            WHERE comments.cid= %s """
    params = (cid, )
    cursor.execute(sql, params)
    ouid = cursor.fetchone()
    cursor.close()
    conn.close()
    return ouid
############################################################
def update_post_like(pos, uid, pid):
    conn, cursor = dbCursor()
    sql = """UPDATE posts_likes 
            SET posts_likes.pos = %s 
            WHERE posts_likes.uid = %s and posts_likes.pid = %s ;"""
    params = (pos, uid, pid)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    
############################################################
def count_post_likes(pid):
    conn, cursor = dbCursor()
    sql ="""select count(pos)
        from posts_likes
        where pid= %s  """
    params = (pid, )
    cursor.execute(sql, params)
    ouid = cursor.fetchone()
    cursor.close()
    conn.close()
    return ouid
############################################################
def check_post_like(uid,pid):
    conn, cursor = dbCursor()
    sql = """Select pos
            From posts_likes
            where uid=  %s  and pid= %s """
    params = (uid,pid)
    cursor.execute(sql, params)
    pos = cursor.fetchone()
    cursor.close()
    conn.close()
#     return whether pos or neg
    return pos

############################################################
def create_post_like(uid, pid, pos, ouid):
    conn, cursor = dbCursor()
    sql = """INSERT INTO posts_likes (uid, pid, pos, ouid)
            VALUES
            ( %s ,  %s ,  %s , %s );"""
    params = (uid, pid, pos, ouid)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()

############################################################
def create_comment_like(uid, cid, pos, ouid):
    conn, cursor = dbCursor()
    sql = """INSERT INTO comments_likes (uid, cid, pos, ouid)
            VALUES
            ( %s ,  %s ,  %s , %s );"""
    params = (uid, cid, pos, ouid)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    
############################################################
def get_post(pid):
    conn, cursor = dbCursor()
    sql =""" SELECT pid, content, pos, neg
        FROM posts
        WHERE posts.pid = %s ;"""
    params = (pid, )
    cursor.execute(sql, params)
    ouid = cursor.fetchone()
    cursor.close()
    conn.close()
    return ouid

############################################################
def get_comments(pid):
    conn, cursor = dbCursor()
    sql =""" SELECT cid, content, pos, neg
        FROM comments
        WHERE pid = %s 
        ORDER BY ts DESC; """
    params = (pid, )
    cursor.execute(sql, params)
    ouid = cursor.fetchall()
    cursor.close()
    conn.close()
    return ouid
############################################################
def create_comment(pid, uid, content):
    conn, cursor = dbCursor()
    sql = """INSERT INTO comments (pid, uid, content)
            VALUES
            ( %s , %s , %s );"""
    params = (pid, uid, content)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
############################################################
def get_regions():
    conn, cursor = dbCursor()
    sql = """SELECT rid, location
    FROM regions;"""
    cursor.execute(sql,)
    regions = cursor.fetchall()
    cursor.close()
    conn.close()
    return regions
############################################################
def get_user(uid):
    conn, cursor = dbCursor()
    sql = """SELECT uid, rid, pos, neg
            FROM users
            WHERE uid= %s """
    params = (uid,)
    cursor.execute(sql, params)
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
############################################################
def count_posts_from_user(uid):
    conn, cursor = dbCursor()
    sql = """SELECT count(pid)
            FROM posts
            where uid = %s ;"""
    params = (uid,)
    cursor.execute(sql, params)
    total = cursor.fetchone()
    cursor.close()
    conn.close()
    return total

############################################################
def get_posts_from_user(uid):
    conn, cursor = dbCursor()
    sql = """SELECT pid, content, comments, pos, neg
            FROM posts
            where uid = %s ;"""
    params = (uid,)
    cursor.execute(sql, params)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
############################################################
def get_posts_from_user_comments(uid):
    conn, cursor = dbCursor()
    sql = """SELECT p.pid, p.content, p.comments, p.pos, p.neg
            FROM posts p, comments
            where comments.uid = %s and p.pid = comments.pid;"""
    params = (uid,)
    cursor.execute(sql, params)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
############################################################
def count_comments_from_user(uid):
    conn, cursor = dbCursor()
    sql = """SELECT count(cid)
            FROM comments
            WHERE uid = %s ;"""
    params = (uid,)
    cursor.execute(sql, params)
    total = cursor.fetchone()
    cursor.close()
    conn.close()
    return total
############################################################
def update_user_region(rid, uid):
    conn, cursor = dbCursor()
    sql = """UPDATE users 
            set rid = %s 
            WHERE uid = %s """
    params = (rid, uid)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()

