from Database.Database import database
from BusinessLayer.ManagerBAl import ManagerBusiness
from tabulate import tabulate


class StudentBusiness:
    def __init__(self, path):
        self.listHeaders = ['Student ID', 'First name', 'Last name', 'Birth day', 'Faculty',
                            'Gender', 'Home town', 'Social Number', 'Phone number', 'School', 'Academic year',
                            'Dormitory name', 'Room name']
        self.database = database(self.listHeaders, [])
        self.path = path
        self.MBA = ManagerBusiness('D:\\DormitoryManagement_Python\\datasets.csv')

    def showScreen(self, IDStudentOption):
        try:
            self.MBA.searchInformationCSV(IDStudentOption)
        except:
            text1 = ["NOTICE"]
            text2 = [['DO NOT FIND THAT STUDENT ID INFORMATION']]
            print(tabulate(text2, text1, tablefmt="pretty"))

    def showAll(self):
        self.database.readCSV('datasets.csv')
