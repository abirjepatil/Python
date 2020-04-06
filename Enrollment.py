from random import choice


class enrollment():
    def __init__(self, StudentID, SeminarID):
        self.StudentID = StudentID
        self.SeminarID = SeminarID

    def Register(self):
        global PoolofNumbers
        PoolofNumbers = []
        for i in range(5):
           PoolofNumbers.append(i+1)

        self. EnrollmentID=choice(PoolofNumbers)
        PoolofNumbers.remove(self.EnrollmentID)
        print(str(self.StudentID)+ "has successfully completed registration of " + str(self.SeminarID))
        print("Your Enrollment ID is AA00500"+str(self.EnrollmentID))
#        for i in range(4):
#            print(PoolofNumbers[i])
        return self.EnrollmentID

    def Unregister(self, EnrollmentID):
        PoolofNumbers.append(self.EnrollmentID)
#        print("After Unregistering:")
#        for i in range(5):
#            print(PoolofNumbers[i])
        print("You have successfully unregistered from the course. Your Enrollment ID was AA00500" +str(EnrollmentID))

