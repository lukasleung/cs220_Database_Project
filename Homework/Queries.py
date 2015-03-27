'''
Created on Mar 22, 2015

@author: Yakisoba
'''
import sys
import sqlite3 as db
import View

# global db connection for ease of coding
filename = "university.db"
conn = db.connect(filename)
cursor = conn.cursor()

def blank_test():
    return True
################################################################################
def update(sql,params=None,test=blank_test,view=View.blank_view):
    success=False
    data=None
    try:
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,params)   
        data = cursor.fetchall()
        success=True
    except:
        success=False
        View.invalid(sys.exc_info()[0])
    finally:
        if success and test():
            conn.commit()
            view(data)
            #View.Success()
        else:
            cursor.rollback()
            View.fail(data)
################################################################################
def retrieval(sql,params=None,view=View.blank_view):
    try:
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,params)
        data = cursor.fetchall()
        view(data)
    except:
        View.invalid(sys.exc_info()[0])   
################################################################################
def disconnect():
    conn.close()
################################################################################
def show_students():
    sql = """select * from Students"""
    params = None   
    view=View.show_students
    retrieval(sql,params,view) 
################################################################################
def show_courses():
    sql = """Select * from Course"""
    params = None
    view=View.show_courses
    retrieval(sql,params,view) 
################################################################################
def show_rooms():
    sql = """select * from Room"""
    params = None
    view = View.show_rooms
    retrieval(sql,params,view) 
################################################################################
def show_departments():
    sql = """select * from Department"""
    params = None
    view=View.show_departments
    retrieval(sql,params,view) 
################################################################################
def show_majors():
    sql = """select * from MajorsIn"""
    params = None
    view = View.show_majors
    retrieval(sql,params,view) 
################################################################################
def add_student(student,name):
    sql = """Insert into Student Values(?,?)"""
    params = (student,name)
    view=View.add_student
    test=blank_test
    update(sql,params,test,view)
################################################################################
def add_course(course,start,end,room):
    sql = """Insert into Course Values (?,?,?,?)"""
    params = (course,start,end,room)
    view = View.add_course
    test=blank_test
    update(sql,params,test,view)
################################################################################
def remove_student(student):
    sql = """Delete from Student where id=?"""
    params = (student,)
    view = View.remove_student
    test=blank_test
    update(sql,params,test,view)
################################################################################
def drop_course(student,course):
    sql = """Delete from Course where student=? AND course = ?"""
    params = (student,course)
    view = View.remove_student
    test=blank_test
    update(sql,params,test,view)
################################################################################
def remove_course(course):
    sql = """Delete from Course where course= ?"""
    params = (course,)
    view = View.remove_course
    test=blank_test
    update(sql,params,test,view)
################################################################################
def enroll_course(student,course,credit):
    sql = """Insert into Enrolled Values (?,?,?)"""
    params = (student,course,credit)
    view = View.enroll_course
    test=blank_test
    update(sql,params,test,view)
################################################################################
def add_major(student,major):
    sql = """Insert into MajorsIn Values (?,?)"""
    params = (student,major)
    view = View.add_major
    test=blank_test
    update(sql,params,test,view)
################################################################################
def remove_major(student,major):
    sql = """Delete from MajorsIn Where student=? AND dept=?"""
    params = (student,major)
    view = View.remove_major
    test=blank_test
    update(sql,params,test,view)
################################################################################
def earliest_start():
    sql = """
    select name, start_time 
    from course c 
    where not exists 
            (select * 
            from course c2 
            where c.start_time<c2.start_time);"""
    params = None
    view = View.earliest_start
    retrieval(sql,params,view)
################################################################################
def room_capacity(capacity=0):
    sql = """select name
            from room
            where capacity >= ?"""
    params = (capacity,)
    view=View.room_capacity
    retrieval(sql,params,view)
################################################################################
