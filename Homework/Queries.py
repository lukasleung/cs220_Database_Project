'''
Created on Mar 22, 2015

@author: Yakisoba
'''
import sys
# import sqlite3 as db
import MySQLdb as db
import View


# global db connection for ease of coding
#filename = "university.db"
# conn = db.connect(filename)
conn = db.connect("localhost", "niwamoto", "niwamoto", "niwamoto")
cursor = conn.cursor()


def blank_test():
    return True

################################################################################
def update(sql, params=None, test=blank_test, view=View.blank_view):
    success = False
    data = None
    try:
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        data = cursor.fetchall()
        success = True
    except:
        success = False
        View.invalid(sys.exc_info())
    finally:
        if success and test():
            conn.commit()
            return view(data)
            # return view.Success()
        else:
            cursor.rollback()
            return view.fail(data)


################################################################################
def retrieval(sql, params=None, view=View.blank_view):
    try:
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        data = cursor.fetchall()
        return view(data)
    except:
        return View.invalid(sys.exc_info())


################################################################################
def disconnect():
    conn.close()


################################################################################
def show_students():
    sql = """SELECT * FROM Student"""
    params = None
    view = View.show_students
    return retrieval(sql, params, view)


################################################################################
def show_courses():
    sql = """SELECT * FROM Course"""
    params = None
    view = View.show_courses
    return retrieval(sql, params, view)


################################################################################
def show_rooms():
    sql = """SELECT * FROM Room"""
    params = None
    view = View.show_rooms
    return retrieval(sql, params, view)


################################################################################
def show_departments():
    sql = """SELECT * FROM Department"""
    params = None
    view = View.show_departments
    return retrieval(sql, params, view)


################################################################################
def show_majors():
    sql = """SELECT * FROM MajorsIn"""
    params = None
    view = View.show_majors
    return retrieval(sql, params, view)


################################################################################
def add_student(student, name):
    sql = """INSERT INTO Student Values( %s , %s )"""
    params = (student, name)
    view = View.add_student
    test = blank_test
    update(sql, params, test, view)


################################################################################
def add_course(course, start, end, room):
    sql = """INSERT INTO Course Values ( %s , %s , %s , %s )"""
    params = (course, start, end, room)
    view = View.add_course
    test = blank_test
    update(sql, params, test, view)


################################################################################
def remove_student(student):
    sql = """DELETE FROM Student WHERE id= %s """
    params = (student,)
    view = View.remove_student
    test = blank_test
    update(sql, params, test, view)


################################################################################
def drop_course(student, course):
    sql = """DELETE FROM Course WHERE student= %s  AND course =  %s """
    params = (student, course)
    view = View.remove_student
    test = blank_test
    update(sql, params, test, view)


################################################################################
def remove_course(course):
    sql = """DELETE FROM Course WHERE course=  %s """
    params = (course,)
    view = View.remove_course
    test = blank_test
    update(sql, params, test, view)


################################################################################
def enroll_course(student, course, credit):
    sql = """INSERT INTO Enrolled Values ( %s , %s , %s )"""
    params = (student, course, credit)
    view = View.enroll_course
    test = blank_test
    update(sql, params, test, view)


################################################################################
def add_major(student, major):
    sql = """INSERT INTO MajorsIn Values ( %s , %s )"""
    params = (student, major)
    view = View.add_major
    test = blank_test
    update(sql, params, test, view)


################################################################################
def remove_major(student, major):
    sql = """DELETE FROM MajorsIn WHERE student= %s  AND dept= %s """
    params = (student, major)
    view = View.remove_major
    test = blank_test
    update(sql, params, test, view)


################################################################################
def earliest_start():
    sql = """
    SELECT name, start_time
    FROM Course c
    WHERE not exists
            (SELECT *
            FROM Course c2
            WHERE c.start_time<c2.start_time);"""
    params = None
    view = View.earliest_start
    return retrieval(sql, params, view)


################################################################################
def room_capacity(capacity=0):
    sql = """SELECT name
            FROM Room
            WHERE capacity >=  %s """
    params = (capacity,)
    view = View.room_capacity
    return retrieval(sql, params, view)

################################################################################
