# This class provides functionality to Conduct a seminar with a professor
class Seminar:
    SeminarId = 0
    ProfessorId = 0
    SeminarName = ''

    def __init__(self, SeminarID, ProfessorId, SeminarName):
        self.ProfessorId = ProfessorId
        self.SeminarId = SeminarID
        self.Name = SeminarName

    def ConductSeminar(self, professorId):
        print("Conducting seminar " + self.SeminarName + str(self.SeminarId) + " With Profesor" + str(professorId))

