from tabulate import tabulate
import csv
import os
import numpy as np

class database:
    def __init__(self, headers, *table):
        self.table = table
        self.headers = headers

    def prettyTable(self):
        print(tabulate(self.table, self.headers, tablefmt="pretty"))

    def writeCSV(self, path):
        list_tmp = []
        with open(path, mode='a', newline='') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            with open(path, mode='r') as employee_file_read:
                for row in csv.reader(employee_file_read):
                    list_tmp.append(row)
                if len(list_tmp) <= 1:
                    employee_writer.writerow(self.headers)
            employee_writer.writerow(*self.table)
            employee_file.close()

    def readCSV(self, path):
        with open(path, 'r') as file:
            reader = csv.reader(file)
            count = 0
            listTables = []
            for row in reader:
                if not row:
                    continue
                listTables.append(row)
            print(tabulate(listTables, [], tablefmt="pretty"))

    def getInformationCSV(self, path):
        list_data = []
        list_train = []
        with open(path, 'r') as file:
            for row in csv.reader(file):
                if not row:
                    continue
                list_data.append(row)
            for i in range(1, len(list_data)):
                if not list_data:
                    continue
                list_train.append(
                    [int(list_data[i][2]), int(list_data[i][3]), int(list_data[i][4]), int(list_data[i][5])])
            list_train = np.array(list_train)

        return list_train
