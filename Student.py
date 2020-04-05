"""
Student class:
variables : name, age, roll, grade
functions : studentdetails(student ID), payfees(amount), feesdue()
"""
from random import randint
class Student:
    def __init__(self, name, age, roll, grade):
        self.name = name
        self.age = age
        self.roll = roll
        self.grade = grade

    def studentdetails(self):

        roll = randint(1, 100)
        student_id = randint(1000, 5000)

        print("Student name is: " + self.name)
        print("Student age is: " + str(self.age))
        print("Student roll number is: " + str(self.roll))
        print("Student grade is: " + self.grade)
        print(self.name + "'s Student ID is: " + str(student_id))

    def studentfeesdetails(self, fees_paid):

        course_fees = 10000
        print("The course fees is: $" + str(course_fees))
        print(self.name + " has paid $" + fees_paid)
        fees_due = course_fees - int(fees_paid)
        print(self.name + " owes $" + str(fees_due))
        return fees_due

# Inputs
print("Enter student name: ")
name = input()

print("Enter student age: ")
age = input()

roll = randint(1, 100)

print("Enter student grade: ")
grade = input()

print(name + " has paid: ")
fees_paid = input()

pupil = Student(name, age, roll, grade)
pupil.studentdetails()
pupil.studentfeesdetails(fees_paid)




