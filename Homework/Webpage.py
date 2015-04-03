#!/usr/bin/python

print "Content-Type: text/html"
print  # a blank line must follow the last HTTP headers

import cgi
import cgitb

cgitb.enable()
import Interface


options = {
    "room_capacity": Interface.room_capacity,
    "earliest_start": Interface.earliest_start,
    "show_students": Interface.show_students,
    "show_courses": Interface.show_courses,
    "show_rooms": Interface.show_rooms,
    "show_departments": Interface.show_departments,
    "show_majors": Interface.show_majors,
    "add_student": Interface.add_student,
    "add_course": Interface.add_course,
    "remove_student": Interface.remove_student,
    "drop_course": Interface.drop_course,
    "remove_course": Interface.remove_course,
    "enroll_course": Interface.enroll_course,
    "add_major": Interface.add_major,
    "remove_major": Interface.remove_major,
}


def web_page(input):
    print """
<html>
<body>

<form method="post">
student:<input type="text" name="student" value=" "><p>
course:<input type="text" name="course" value=" "><p>
start:<input type="text" name="start" value=" "><p>
end:<input type="text" name="end" value=" "><p>
room:<input type="text" name="room" value=" "><p>
major:<input type="text" name="major" value=" "><p>
capacity:<input type="text" name="capacity" value=" "><p>
name:<input type="text" name="name" value=" "><p>
credit:<input type="text" name="credit" value=" "><p>

<input type="radio" name="action" value="room_capacity">room_capacity<br>
<input type="radio" name="action" value="earliest_start">earliest_start<br>
<input type="radio" name="action" value="show_students">show_students<br>
<input type="radio" name="action" value="show_courses">show_courses<br>
<input type="radio" name="action" value="show_rooms">show_rooms<br>
<input type="radio" name="action" value="show_departments">show_departments<br>
<input type="radio" name="action" value="show_majors">show_majors<br>
<input type="radio" name="action" value="add_student">add_student<br>
<input type="radio" name="action" value="add_course">add_course<br>
<input type="radio" name="action" value="remove_student">remove_student<br>
<input type="radio" name="action" value="drop_course">drop_course<br>
<input type="radio" name="action" value="remove_course">remove_course<br>
<input type="radio" name="action" value="enroll_course">enroll_course<br>
<input type="radio" name="action" value="add_major">add_major<br>
<input type="radio" name="action" value="remove_major">remove_major<br>
<input type="radio" name="action" value="end">end<br>

<input type="submit" name="Go" value="Go"></form>

Output:
<table border="1" style"width:5ds0%">
  <tr>
    <th><p> {0}<p></th>
  </tr>
</table>


</body>
</html>""".format(input)


if __name__ == "__main__":
    form = cgi.FieldStorage()

    #form.has_key("GO!")
    if "Go" in form and form["Go"].value == "Go" and "action" in form:

        # if "action" in form:
        #     print "Action is here!", form["action"].value + "<p>"
        # else:
        #     print "NO ACTION!!!"
        #
        # if "student" in form:
        #     print "student is here!", form["student"].value + "<p>"
        #
        # else:
        #     print "NOOOoooooo!"

        student = str(form["student"].value)
        course = str(form["course"].value)
        start = str(form["start"].value)
        end = str(form["end"].value)
        room = str(form["room"].value)
        major = str(form["major"].value)
        capacity = str(form["capacity"].value)
        name = str(form["name"].value)
        credit = str(form["credit"].value)

        params = (student, course, start, end, room, major, capacity, name, credit)

        func = options[form["action"].value]

        results = str(func(params))
        web_page(results)
    else:
        web_page("output")