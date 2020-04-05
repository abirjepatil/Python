"""
This it the controller class
Reponsibe for 
a) Creating Students 
b) Creating Seminar
c) Creating Profesors
e) Enrolling Students
"""
from Student import Student


class Controller:
    global students
    students = {}

    def __init__(self):
        self.students = {}

    # This is a dictionary of all students. The key is the roll number and value is student object.
    def PrintAllStudents(self):
        print(self.students)

    def CreateStudent(self, name, age, roll, grade):
        global students  # dictionary of all students
        studentObj = Student(name, age, roll, grade)  # each student
        self.students[roll] = studentObj


############################################################################################
## ADDING ALL STUDENTS TO THE DICTIONARY
############################################################################################

ctrl = Controller()
ctrl.CreateStudent("Abhi", 20, 1, "A")
ctrl.CreateStudent("Parth", 21, 2, "A++")
ctrl.CreateStudent("Shriyanka", 22, 3, "A+")
ctrl.CreateStudent("Sud", 23, 4, "A-")
############################################################################################

############################################################################################
## PRINTING ALL STUDENTS
############################################################################################

for key in ctrl.students:
    print(key)
    ctrl.students[key].studentdetails()
############################################################################################
############################################################################################