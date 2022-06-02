from View.ManagerView import ManagerView
from View.StudentView import StudentView
from tabulate import tabulate


def main():
    while True:
        print("***************************************************************************************************\n")
        print("*                                                                                                 *\n")
        print("*             HCMC University of Technology and Education Dormitory Management System             *\n")
        print("*                                                                                                 *\n")
        print("*                                    1. Function for manager                                      *\n")
        print("*                                    2. Function for student                                      *\n")
        print("***************************************************************************************************\n")
        option = int(input("Input your option: "))
        if option == 1:
            MV = ManagerView("admin", "12345")
            MV.loginScreen()
            MV.menuForManager()
        elif option == 2:
            SV = StudentView()
            SV.showAllInformation()
            SV.getInformationIDStudent()
        elif option == 0:
            exit(0)
        else:
            text1 = ["NOTICE"]
            text2 = [["Wrong keyword, please try again !"], ['If you want to exit, press number 0 !']]
            print(tabulate(text2, text1, tablefmt="pretty"))


if __name__ == '__main__':
    main()
