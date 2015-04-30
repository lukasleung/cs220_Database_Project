import MySQLdb as db

# global db connection for ease of coding
#filename = "university.db"
# conn = db.connect(filename)


# deletes and recreates the database
def remove_tables():
    pass

def create_tables():
#     create tables
#     create triggers
    pass

def insert_dummy():
    pass

def login_page():
    conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
    cursor = conn.cursor()
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

def add_user(rid):
    conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
    cursor = conn.cursor()
    sql = """INSERT INTO users (rid)
            VALUES
            ( %s );"""
    params = (rid, )
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    
def posts_region(rid, order_rule="recent"):
    conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
    cursor = conn.cursor()
    sql = """SELECT pid, content, comments, pos, neg
            FROM posts
            WHERE posts.rid= %s"""
    if order_rule == "recent":
        sql+= "ORDER BY posts.ts DESC;"
    elif order_rule == "positive":
        sql+= "ORDER BY posts.pos DESC;"
    elif order_rule == "negative":
        sql+= "ORDER BY posts.neg DESC;"
    elif order_rule == "controversial": 
        sql+= "ORDER BY abs((1/16)-(power((pos/(pos+neg)),3)+ power((neg/(pos+neg)),3)));"
    elif order_rule == "comments":
        sql+= "ORDER BY posts.comments DESC;"
    elif order_rule == "interaction":
        sql+= "ORDER BY posts.pos+posts.neg+posts.comments DESC;"
    else:
        sql+= "ORDER BY posts.ts DESC;"
    params = (rid, )
    cursor.execute(sql, params)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
    
def create_post(uid, content, rid):
    conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
    cursor = conn.cursor()
    sql = """INSERT INTO posts (uid, content, rid)
            VALUES
            ( %s ,  %s , %s );"""
    params = (uid, content, rid)
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    conn.close()
    