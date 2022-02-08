Course_room = {
    "Course Number": "Room Number",
    "CS101": "3004",
    "CS102": "4501",
    "CS201": "6755",
    "NT110": "1244",
    "CM241": "1411",
}

# print(Course_room)

Course_instructor = {
    "Course Number": "Instructor",
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS201": "Rich",
    "NT110": "Burke",
    "CM241": "Lee",
}

# print(Course_instrucor)

Course_time = {
    "Course Number": "Meeting Time",
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS201": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m.",
}

# print(Course_time)

course_num = input("Please enter a course number: ")

if course_num in Course_room:
    print("Room number:", Course_room[course_num])

    if course_num in Course_instructor:
        print("Instructor:", Course_instructor[course_num])

    if course_num in Course_time:
        print("Time:", Course_time[course_num])

else:
    print("Course number not found")
