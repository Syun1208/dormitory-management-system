from BusinessLayer.StudentBAl import StudentBusiness


class StudentView:
    def __init__(self):
        self.SBA = StudentBusiness('datasets.csv')

    def getInformationIDStudent(self):
        optionIDStudent = input("Input your Student ID you want to find related to your input: ")
        self.SBA.showScreen(optionIDStudent)

    def showAllInformation(self):
        self.SBA.showAll()
