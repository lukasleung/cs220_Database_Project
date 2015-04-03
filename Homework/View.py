'''
Created on Feb 27, 2015

@author: Yakisoba
'''


def blank_view():
    output = "TEXT HERE" + "<p>"


################################################################################
def format_students(data=None):
    output = "Student Name".ljust(15) + "<p>"
    for name in data:
        output += str(name).ljust(15) + "<p>"
    return output 


################################################################################
def format_courses(data=None):
    output = "Course Name".ljust(15) + "Start Time".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + "<p>"
    return output 


################################################################################
def invalid(data=None):
    output = "Invalid: " + str(data) + "<p>"
    return output 


################################################################################
def fail(data=None):
    output = "failed: ", data + "<p>"
    return output 


################################################################################
def success(data=None):
    output = "Done!", data + "<p>"
    return output 


################################################################################
def show_students(data):
    output = "Student ID".ljust(15) + "Student Name".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + "<p>"
    return output 


################################################################################
def show_courses(data):
    output = "Course Name".ljust(15) + "Start Time".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + "<p>"
    return output 


################################################################################
def show_rooms(data):
    output = "Course ID".ljust(15) + "Course Name".ljust(20) + "Capacity".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + str(name[2]).ljust(20) + "<p>"
    return output 


################################################################################
def show_departments(data):
    output = "Course Name".ljust(15) + "Start Time".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + "<p>"
    return output 


################################################################################
def show_majors(data):
    output = "Student".ljust(15) + "Major".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + "<p>"
    return output 


################################################################################
def add_student(data):
    return success(data)


################################################################################
def add_course(data):
    return success(data)


################################################################################
def remove_student(data):
    return success(data)


################################################################################
def remove_course(data):
    return success(data)


################################################################################
def enroll_course(data):
    return success(data)


################################################################################
def add_major(data):
    return success(data)


################################################################################
def remove_major(data):
    return success(data)


################################################################################
def room_capacity(data):
    output = "name" + "<p>"
    for name in data:
        output += str(name) + "<p>"
    return output 


################################################################################
def earliest_start(data):
    output = "Course Name".ljust(15) + "Start Time".ljust(20) + "<p>"
    for name in data:
        output += str(name[0]).ljust(15) + str(name[1]).ljust(20) + "<p>"
    return output 
    ################################################################################