import csv
from tabulate import tabulate
from Database.Database import database
import numpy as np
import matplotlib.pyplot as plt


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i][12]
        j = i - 1
        while j >= 0 and key < int(arr[j][12]):
            arr[j + 1][12] = int(arr[j][12])
            j -= 1
        arr[j + 1][12] = key


def selection_sort(L):
    for i in range(0, len(L) - 1):
        min_index = i
        for j in range(i + 1, len(L)):
            if int(L[j][12]) < int(L[min_index][12]):
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L
    # print(tabulate(L, tablefmt="pretty"))


class KMeansClustering:
    def __init__(self, X, num_clusters):
        self.K = num_clusters
        self.max_iterations = 100
        self.plot_figure = True
        self.num_examples = X.shape[0]
        self.num_features = X.shape[1]

    def initialize_random_centroids(self, X):
        centroids = np.zeros((self.K, self.num_features))

        for k in range(self.K):
            centroid = X[np.random.choice(range(self.num_examples))]
            centroids[k] = centroid

        return centroids

    def create_clusters(self, X, centroids):
        # Will contain a list of the points that are associated with that specific cluster
        clusters = [[] for _ in range(self.K)]

        # Loop through each point and check which is the closest cluster
        for point_idx, point in enumerate(X):
            closest_centroid = np.argmin(
                np.sqrt(np.sum((point - centroids) ** 2, axis=1))
            )
            clusters[closest_centroid].append(point_idx)

        return clusters

    def calculate_new_centroids(self, clusters, X):
        centroids = np.zeros((self.K, self.num_features))
        for idx, cluster in enumerate(clusters):
            new_centroid = np.mean(X[cluster], axis=0)
            centroids[idx] = new_centroid

        return centroids

    def predict_cluster(self, clusters, X):
        y_pred = np.zeros(self.num_examples)

        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                y_pred[sample_idx] = cluster_idx

        return y_pred

    def plot_fig(self, X, y):
        plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
        plt.show()

    def fit(self, X):
        centroids = self.initialize_random_centroids(X)

        for it in range(self.max_iterations):
            clusters = self.create_clusters(X, centroids)

            previous_centroids = centroids
            centroids = self.calculate_new_centroids(clusters, X)

            diff = centroids - previous_centroids

            if not diff.any():
                print("Termination criterion satisfied")
                break

        # Get label predictions
        y_pred = self.predict_cluster(clusters, X)

        if self.plot_figure:
            self.plot_fig(X, y_pred)

        return y_pred


class ManagerBusiness:
    def __init__(self, path):
        self.path = path

    def deleteInformationCSV(self, IDStudentOption):
        lines = []
        results = []
        listHeaders = ['Student ID', 'First name', 'Last name', 'Birth day', 'Faculty',
                       'Gender', 'Home town', 'Social Number', 'Phone number', 'School', 'Academic year',
                       'Dormitory name', 'Room name']
        with open(self.path, mode='r') as inp, open("output.csv", mode='w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                lines.append(row)
            for i in range(1, len(lines)):
                if not lines[i]:
                    continue
                elif lines[i][0] != IDStudentOption:
                    writer.writerow(lines[i])
        with open("output.csv", mode='r') as save, open(self.path, mode='w') as save_main:
            tmp = []
            writer = csv.writer(save_main)
            for row in csv.reader(save):
                tmp.append(row)
            if len(tmp) <= 1:
                writer.writerow(listHeaders)
            for i in range(0, len(tmp)):
                if not tmp[i]:
                    continue
                if len(tmp[i]) <= 1:
                    writer.writerow(listHeaders)
                writer.writerow(tmp[i])
                results.append(tmp[i])
            print(tabulate(results, [], tablefmt="pretty"))

    def delete(self, IDStudentOption):
        lines = []
        results = []
        # listHeaders = ['Student ID', 'First name', 'Last name', 'Birth day', 'Faculty',
        #                'Gender', 'Home town', 'Social Number', 'Phone number', 'School', 'Academic year',
        #                'Dormitory name', 'Room name']
        with open(self.path, mode='r') as inp, open("output.csv", mode='w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                lines.append(row)
            for i in range(1, len(lines)):
                if not lines[i]:
                    continue
                elif lines[i][0] != IDStudentOption:
                    writer.writerow(lines[i])
        with open("output.csv", mode='r') as save, open(self.path, mode='w') as save_main:
            tmp = []
            writer = csv.writer(save_main)
            for row in csv.reader(save):
                tmp.append(row)
            for i in range(0, len(tmp)):
                if not tmp[i]:
                    continue
                writer.writerow(tmp[i])
                results.append(tmp[i])

    def sortInformationCSV(self):
        list_tmp = []
        with open(self.path, mode='r') as sort_csv:
            for row in csv.reader(sort_csv):
                if not row:
                    continue
                list_tmp.append(row)
            results = selection_sort(list_tmp)
        with open(self.path, mode='w') as save_sort:
            write = csv.writer(save_sort)
            for i in range(len(results)):
                if not results:
                    continue
                write.writerow(results[i])
        print(tabulate(results, [], tablefmt="pretty"))
        # insertionSort(list_tmp)

    def searchInformationCSV(self, searchStudentIDOption):
        list_tmp = list()
        listHeaders = ['Student ID', 'First name', 'Last name', 'Birth day', 'Faculty',
                       'Gender', 'Home town', 'Social Number', 'Phone number', 'School', 'Academic year',
                       'Dormitory name', 'Room name']
        with open(self.path, mode='r') as sort_csv:
            for row in csv.reader(sort_csv):
                list_tmp.append(row)
            for i in range(0, len(list_tmp)):
                if not list_tmp[i]:
                    continue
                elif list_tmp[i][0] == searchStudentIDOption:
                    print(tabulate([list_tmp[i]], listHeaders, tablefmt="pretty"))

    def editInformationCSV(self, editStudentIDOption):
        list_tmp = list()
        list_edit = []
        listHeaders = ['Student ID', 'First name', 'Last name', 'Birth day', 'Faculty',
                       'Gender', 'Home town', 'Social Number', 'Phone number', 'School', 'Academic year',
                       'Dormitory name', 'Room name']
        with open(self.path, mode='r') as sort_csv:
            for row in csv.reader(sort_csv):
                list_tmp.append(row)
            for i in range(1, len(list_tmp)):
                if not list_tmp[i]:
                    continue
                elif list_tmp[i][0] == editStudentIDOption:
                    list_tmp[i][0] = editStudentIDOption
                    list_tmp[i][1] = input("Input First Name: ")
                    list_tmp[i][2] = input("Input Last Name: ")
                    list_tmp[i][3] = input("Birthday: ")
                    list_tmp[i][4] = input("Faculty: ")
                    list_tmp[i][5] = input("Gender: ")
                    list_tmp[i][6] = input("Home town: ")
                    list_tmp[i][7] = input("Social Number: ")
                    list_tmp[i][8] = input("Phone number: ")
                    list_tmp[i][9] = input("School: ")
                    list_tmp[i][10] = input("School year: ")
                    list_tmp[i][11] = input("Dormitory name: ")
                    list_tmp[i][12] = input("Room Name: ")
            list_result = []
            for i in range(0, len(list_tmp)):
                if not list_tmp[i]:
                    continue
                else:
                    list_edit.append(list_tmp[i])
            for j in range(0, len(list_edit)):
                if list_edit[j][0] == editStudentIDOption:
                    list_result.append(list_edit[j])
            self.delete(editStudentIDOption)
            for h in range(len(list_result)):
                database_edit = database(listHeaders, list_result[h])
            database_edit.writeCSV(self.path)
            print(tabulate(list_edit, tablefmt="pretty"))

    def countInformationCSV(self):
        list_tmp = []
        with open(self.path, mode='r') as count_csv:
            for row in csv.reader(count_csv):
                list_tmp.append(row)
        count = 0
        list_count = []
        for i in range(len(list_tmp)):
            for j in range(len(list_tmp)):
                if list_tmp[i][12] == list_tmp[j][12]:
                    count = count + 1
                else:
                    count = 0
            list_count.append(count)
        print(list_count)
        # text1 = ["NOTICE"]
        # print(tabulate([list_tmp], text1, tablefmt="pretty"))

    def statisticInformationCSV(self, path):
        list_tmp = []
        list_total = []
        list_results = []
        with open(path, mode='r') as statistic_csv:
            for row in csv.reader(statistic_csv):
                list_tmp.append(row)
            for i in range(1, len(list_tmp)):
                if not list_tmp[i]:
                    continue
                list_tmp[i][5] = int(list_tmp[i][2]) * 50 + int(list_tmp[i][3]) * 20 + int(list_tmp[i][4])
                list_total.append(list_tmp[i][5])
            for i in range(1, len(list_tmp)):
                list_results.append(list_tmp[i])
        with open(path, mode='w') as save_statistic:
            write = csv.writer(save_statistic)
            for i in range(len(list_tmp)):
                if not list_tmp[i]:
                    continue
                write.writerow(list_tmp[i])

        print(tabulate(list_results, list_tmp[0], tablefmt="pretty"))

    def standardEvaluationInformation(self, path_evaluation):
        np.random.seed(10)
        databases = database([], [])
        X = np.random.random((1000, 2))
        list_data = databases.getInformationCSV(path_evaluation)
        num_clusters = int(input("Input the number of clusters: "))
        KM = KMeansClustering(X, num_clusters)
        prediction = KM.fit(X)
        print("Prediction: {}".format(prediction))
