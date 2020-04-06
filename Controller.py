"""
This it the controller class
Reponsibe for 
a) Creating Students 
b) Creating Seminar
c) Creating Profesors
e) Enrolling Students
"""
from Student import Student
from Professor import  Professor
from Seminar import Seminar

class Controller:
    global students
    students = {}
    professors = {}
    seminars = {}
    enrollments ={}

    def __init__(self):
        self.students = {}
        self.professors = {}
        self.seminars = {}
        self.enrollments ={}

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
# Creating Seminars
seminar1 = Seminar(1,1,"Learn Stock Investing")
seminar2 = Seminar(2,1,"Learn data analytics online")
seminar3 = Seminar(3,2,"Learn Adobe Photoshop")
seminar4 = Seminar(4,3,"Learn Pycharms")

ctrl.seminars[1] = seminar1
ctrl.seminars[2] = seminar2
ctrl.seminars[3] = seminar3
ctrl.seminars[4] = seminar4

print(ctrl.seminars)
############################################################################################
############################################################################################
prof1 = Professor(1, "John Doe")
prof2 = Professor(2, "Alex Shaw")

ctrl.professors[1] = prof1
ctrl.professors[2] = prof2
print(ctrl.professors)
############################################################################################
############################################################################################

Enrollment1 = enrollment(1, 1)

ID=Enrollment1.Register()

ctrl.enrollments[ID]=Enrollment1

############################################################################################
############################################################################################
