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
    
def posts_region(rid, order_rule="posts.ts"):
    conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
    cursor = conn.cursor()
    sql = """SELECT pid, content, comments, pos, neg
            FROM posts
            WHERE posts.rid= %s 
            ORDER BY %s ;"""
    params = (rid,order_rule )
    cursor.execute(sql, params)
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return posts
    
    