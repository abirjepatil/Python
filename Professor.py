# This class provides functionality to grade students.
# It returns a dictionary of students and grades.
class Professor:
    Name = ''
    ProfessorId = 0

    def __init__(self, ProfessorId, Name):
        self.Name = Name
        self.ProfessorId = ProfessorId

    def GradeStudensts(self, SeminarId,Students):
        thisdict = {
            "StudentA": "A+",
            "StudentB": "B",
            "StudentC": "C"
        }
        return thisdict

