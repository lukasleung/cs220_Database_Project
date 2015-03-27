'''
Created on Mar 22, 2015

@author: Yakisoba

'''

#make interactive program with university database from quiz 3 commands plus your own commands

import Queries

################################################################################
def show_students():
    Queries.show_students()
################################################################################
def show_courses():
    Queries.show_courses()
################################################################################
def show_rooms():
    Queries.show_rooms()
################################################################################
def show_departments():
    Queries.show_departments()
################################################################################
def show_majors():
    Queries.show_majors()
################################################################################
def add_student():
    student = input("Enter the Student's id: ")
    name = input("Enter the student's name: ")
    Queries.add_student(student,name)
################################################################################
def add_course():
    course = input("Enter the course name: ")
    start = input("Enter the start time: ") 
    end = input("Enter the end time: ") 
    room = input("Enter the room number: ") 
    Queries.add_course(course,start,end,room)
################################################################################
def remove_student():
    student = input("Enter the Student's id: ")
    Queries.remove_student(student)
################################################################################
def drop_course():
    student = input("Enter the Student's id: ")
    course = input("Enter the course name: ")
    Queries.drop_course(student,course)
################################################################################
def remove_course():
    course = input("Enter the course name: ") 
    Queries.remove_course(course)
################################################################################
def enroll_course():
    student = input("Enter the Student's id: ")
    course = input("Enter the course name: ")
    credit = input("Enter the course's credit status: ")
    Queries.enroll_course(student,course,credit)
################################################################################
def add_major():
    student = input("Enter the Student's id: ")
    major = input("Enter the major: ")
    Queries.add_major(student,major)
################################################################################
def remove_major():
    student = input("Enter the Student's id: ")
    major = input("Enter the major: ")
    Queries.remove_major(student,major)
################################################################################
def room_capacity(): 
    capacity = input("Enter capacity's lower limit: ")
    Queries.room_capacity(capacity)
################################################################################
def earliest_start():
    Queries.earliest_start()
################################################################################  
def end():
    Queries.disconnect()
    print "Goodbye!"
################################################################################
if __name__ == "__main__":

    # a main program loop:

    choice = "foo"

    while choice.lower()[0] != "q":

        print """
        University: Please select an option:
        (a) room_capacity()
        (b) earliest_start()
        (c) show_students()
        (d) show_courses()
        (e) show_rooms()
        (f) show_departments()
        (g) show_majors()
        (h) add_student()
        (i) add_course()
        (j) remove_student()
        (k) drop_course()
        (l) remove_course()
        (m) enroll_course()
        (n) remove_course()
        (o) add_major() 
        (p) remove_major()
        (q) end

        """
        
        choice = raw_input("> ")

        if choice.lower()[0] == "a":
            room_capacity()
        elif choice.lower()[0] == "b":
            earliest_start()
        elif choice.lower()[0] == "c":
            show_students()
        elif choice.lower()[0] == "d":
            show_courses()
        elif choice.lower()[0] == "e":
            show_rooms()
        elif choice.lower()[0] == "f":
            show_departments()
        elif choice.lower()[0] == "g":
            show_majors()
        elif choice.lower()[0] == "h":
            add_student()
        elif choice.lower()[0] == "i":
            add_course()
        elif choice.lower()[0] == "j":
            remove_student()
        elif choice.lower()[0] == "k":
            drop_course()
        elif choice.lower()[0] == "l":
            remove_course()
        elif choice.lower()[0] == "m":
            enroll_course()
        elif choice.lower()[0] == "n":
            remove_course()
        elif choice.lower()[0] == "o":
            add_major()
        elif choice.lower()[0] == "p":
            remove_major()
        elif choice.lower()[0] == "q":
            end()
            break
        # end of the loop
        
