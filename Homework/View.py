'''
Created on Feb 27, 2015

@author: Yakisoba
'''

def blank_view():
    print "TEXT HERE"
################################################################################
def formatStudents (data=None):
    print "Student Name".ljust(15)
    for name in data:
        print str(name).ljust(15)
################################################################################
def formatCourses (data=None):
    print "Course Name".ljust(15) + "Start Time".ljust(20)
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)
################################################################################
def invalid (data=None):
    print "Invalid: ", data
################################################################################
def fail (data=None):
    print "failed: ", data
################################################################################
def success (data=None):
    print "Done!", data
################################################################################
def show_students(data):
    print "Student ID".ljust(15) + "Student Name".ljust(20)
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)
################################################################################
def show_courses(data):
    print "Course Name".ljust(15) + "Start Time".ljust(20)
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)
################################################################################
def show_rooms(data):
    print "Course ID".ljust(15) + "Course Name".ljust(20) + "Capacity".ljust(20) 
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)+ str(name[2]).ljust(20)
################################################################################
def show_departments(data):
    print "Course Name".ljust(15) + "Start Time".ljust(20)
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)
################################################################################
def show_majors(data):
    print "Student".ljust(15) + "Major".ljust(20)
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)
################################################################################
def add_student(data):
    success (data)
################################################################################
def add_course(data):
    success (data)
################################################################################
def remove_student(data):
    success (data)
################################################################################
def remove_course(data):
    success (data)
################################################################################
def enroll_course(data):
    success (data)
################################################################################
def add_major(data):
    success (data)
################################################################################
def remove_major(data):
    success (data)
################################################################################
def room_capacity(data):
    print "name"
    for name in data:
        print str(name)
################################################################################
def earliest_start(data):
    print "Course Name".ljust(15) + "Start Time".ljust(20)
    for name in data:
        print str(name[0]).ljust(15)+ str(name[1]).ljust(20)
################################################################################