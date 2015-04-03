'''
Created on Mar 22, 2015

@author: Yakisoba

'''

# make interactive program with university database from quiz 3 commands plus your own commands

import Queries

################################################################################
def show_students(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    return Queries.show_students()


################################################################################
def show_courses(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    return Queries.show_courses()


################################################################################
def show_rooms(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    return Queries.show_rooms()


################################################################################
def show_departments(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    return Queries.show_departments()


################################################################################
def show_majors(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    return Queries.show_majors()


################################################################################
def add_student(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # student = input("Enter the Student's id: ")
    # name = input("Enter the student's name: ")
    return Queries.add_student(student, name)


################################################################################
def add_course(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # course = input("Enter the course name: ")
    # start = input("Enter the start time: ")
    # end = input("Enter the end time: ")
    # room = input("Enter the room number: ")
    return Queries.add_course(course, start, end, room)


################################################################################
def remove_student(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # student = input("Enter the Student's id: ")
    return Queries.remove_student(student)


################################################################################
def drop_course(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # student = input("Enter the Student's id: ")
    # course = input("Enter the course name: ")
    return Queries.drop_course(student, course)


################################################################################
def remove_course(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # course = input("Enter the course name: ")
    return Queries.remove_course(course)


################################################################################
def enroll_course(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # student = input("Enter the Student's id: ")
    # course = input("Enter the course name: ")
    # credit = input("Enter the course's credit status: ")
    return Queries.enroll_course(student, course, credit)


################################################################################
def add_major(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # student = input("Enter the Student's id: ")
    # major = input("Enter the major: ")
    return Queries.add_major(student, major)


################################################################################
def remove_major(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # student = input("Enter the Student's id: ")
    # major = raw_input("Enter the major: ")
    return Queries.remove_major(student, major)


################################################################################
def room_capacity(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    # capacity = input("Enter capacity's lower limit: ")
    return Queries.room_capacity(capacity)


################################################################################
def earliest_start(params=(1, 2, 3, 4, 5, 6, 7, 8, 9)):
    student, course, start, end, room, major, capacity, name, credit = params
    return Queries.earliest_start()


################################################################################
def end():
    Queries.disconnect()
    print "Goodbye!"

################################################################################
def menu():
# if __name__ == "__main__":

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
        (n) add_major()
        (o) remove_major()
        (p) end

        """

        choice = raw_input("> ").lower()[0]

        if choice.lower()[0] == "a":
            print room_capacity()
        elif choice.lower()[0] == "b":
            print earliest_start()
        elif choice.lower()[0] == "c":
            print show_students()
        elif choice.lower()[0] == "d":
            print show_courses()
        elif choice.lower()[0] == "e":
            print show_rooms()
        elif choice.lower()[0] == "f":
            print show_departments()
        elif choice.lower()[0] == "g":
            print show_majors()
        elif choice.lower()[0] == "h":
            print add_student()
        elif choice.lower()[0] == "i":
            print add_course()
        elif choice.lower()[0] == "j":
            print remove_student()
        elif choice.lower()[0] == "k":
            print drop_course()
        elif choice.lower()[0] == "l":
            print remove_course()
        elif choice.lower()[0] == "m":
            print enroll_course()
        elif choice.lower()[0] == "n":
            print add_major()
        elif choice.lower()[0] == "o":
            print remove_major()
        elif choice.lower()[0] == "p":
            print end()
            break
            # end of the loop
        
