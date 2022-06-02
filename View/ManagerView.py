from Datasets.Student import Student
from Datasets.Manager import Manager
from Database.Database import database
from BusinessLayer.ManagerBAl import ManagerBusiness
from tabulate import tabulate


class ManagerView(Manager, Student):
    def __init__(self, userName, passWord):
        super(ManagerView, self).__init__(userName, passWord)
        self.MBA = ManagerBusiness('D:\\DormitoryManagement_Python\\datasets.csv')
        self.listHeaders = ['Student ID', 'First name', 'Last name', 'Birth day', 'Faculty',
                            'Gender', 'Home town', 'Social Number', 'Phone number', 'School', 'Academic year',
                            'Dormitory name', 'Room name']

    def loginScreen(self):
        condition = True
        n = 0
        while condition:
            print("======================Log in=========================\n")
            userLogin = input("User Name: \n")
            passWordLogin = input("Password: \n")
            if userLogin == self.userName and passWordLogin == self.passWord:
                print("Login successfully !")
                condition = False
            else:
                print("Wrong Password !")
                n = n + 1
                condition = True
                if n == 3:
                    print("You do not have any choices !")
                    exit(0)

    def menuForManager(self):
        print("***************************************************************************************************\n")
        print("*                                                                                                 *\n")
        print("*             HCMC University of Technology and Education Dormitory Management System             *\n")
        print("*                                                                                                 *\n")
        print("*                                    1. Adding student                                            *\n")
        print("*                                    2. Deleting student                                          *\n")
        print("*                                    3. Search                                                    *\n")
        print("*                                    4. Statistic                                                 *\n")
        print("*                                    5. Show information                                          *\n")
        print("*                                    6. Modify                                                    *\n")
        print("*                                    7. Standard Evaluation                                       *\n")
        print("*                                    8. Sort                                                      *\n")
        print("*                                    9. Exit                                                      *\n")
        print("***************************************************************************************************\n")
        while True:
            option = -1
            option = int(input("Input your option: "))
            if option == 1:
                self.addStudentScreen()
            elif option == 2:
                self.deleteStudentScreen()
            elif option == 3:
                self.searchScreen()
            elif option == 4:
                self.statisticScreen()
            elif option == 5:
                self.showScreen()
            elif option == 6:
                self.editScreen()
            elif option == 7:
                self.standardEvaluationScreen()
            elif option == 8:
                self.sortScreen()
            elif option == 9:
                exit(0)
            else:
                text1 = ["NOTICE"]
                text2 = [["Wrong keyword, please try again !"], ["If you want to exit, press number 7 !"]]
                print(tabulate(text2, text1, tablefmt="pretty"))

    def addStudentScreen(self):
        listStudent = []
        self.ID = input("Input Student ID: ")
        self.firstName = input("Input First Name: ")
        self.lastName = input("Input Last Name: ")
        self.birthDay = input("Input your birthday: ")
        self.birthMonth = input("Input your birth month: ")
        self.birthYear = input("Input your birth year: ")
        self.faculty = input("Faculty: ")
        self.gender = input("Gender: ")
        self.homeTown = input("Home town: ")
        self.socialNumber = input("Social Number: ")
        self.phoneNumber = input("Phone number: ")
        self.school = input("School: ")
        self.schoolYear = input("School year: ")
        self.placeStudent.DormitoryData.nameDormitory = input("Dormitory name: ")
        self.placeStudent.RoomData.ID = int(input("Room ID: "))
        self.placeStudent.DormitoryData.floorNumber = int(input("Floor number: "))
        listStudent.extend(
            [self.ID, self.firstName, self.lastName, self.birthDay + '/' + self.birthMonth + '/' + self.birthYear,
             self.faculty, self.gender, self.homeTown, self.socialNumber, self.phoneNumber, self.school,
             self.schoolYear, self.placeStudent.DormitoryData.nameDormitory,
             self.placeStudent.RoomData.ID + self.placeStudent.DormitoryData.floorNumber * 100])
        try:
            databaseStudent = database(self.listHeaders, listStudent)
            databaseStudent.prettyTable()
            databaseStudent.writeCSV('datasets.csv')
            print("Information is already saved in datasets.csv")
        except:
            text1 = ["NOTICE"]
            text2 = [['PLEASE CLOSE YOUR FILE CSV ON TASK BAR ! YOUR INPUT WILL NOT BE SAVED IN FILE CSV !TRY AGAIN !']]
            print(tabulate(text2, text1, tablefmt="pretty"))

    def deleteStudentScreen(self):
        optionIDStudent = input("Input Student ID you want to delete: ")
        try:
            self.MBA.deleteInformationCSV(optionIDStudent)
        except:
            text1 = ["NOTICE"]
            text2 = [['DO NOT FIND THAT STUDENT ID']]
            print(tabulate(text2, text1, tablefmt="pretty"))

    def showScreen(self):
        databaseShow = database(self.listHeaders, [])
        databaseShow.readCSV('datasets.csv')
        # self.MBA.countInformationCSV()

    def sortScreen(self):
        self.MBA.sortInformationCSV()

    def searchScreen(self):
        IDOption = input("Input Student ID you want to search: ")
        try:
            self.MBA.searchInformationCSV(IDOption)
        except:
            text1 = ["NOTICE"]
            text2 = [['DO NOT FIND THAT STUDENT ID INFORMATION']]
            print(tabulate(text2, text1, tablefmt="pretty"))

    def editScreen(self):
        try:
            editOptionIDStudent = input("Input Student ID you want to edit: ")
            self.MBA.editInformationCSV(editOptionIDStudent)
        except:
            text1 = ["NOTICE"]
            text2 = [['DO NOT FIND THAT STUDENT ID INFORMATION']]
            print(tabulate(text2, text1, tablefmt="pretty"))

    def statisticScreen(self):
        self.MBA.statisticInformationCSV("StatisticMoney.csv")

    def standardEvaluationScreen(self):
        self.MBA.standardEvaluationInformation('KMeansData.csv')
