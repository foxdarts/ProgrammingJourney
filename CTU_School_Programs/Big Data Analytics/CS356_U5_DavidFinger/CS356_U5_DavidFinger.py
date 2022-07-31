# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:22:59 2020

@author: foxsq
"""

import pandas as PD
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

Data = open(r"C:\Users\foxsq\OneDrive\Documents\ctu school stuff\Big Data Analytics\Demographic_Statistics_By_Zip_Code.csv") #demographic data csv
Demo = PD.read_csv(Data)

Demo.head()

print("Data Shape: ", Demo.shape) #gives shape of csv file.

X = Demo.iloc[:, : -1]
Y = Demo.iloc[:, -1] #takes data and ets it up for KNN split

X_train, X_Test, Y_train, Y_Test = train_test_split(X, Y, test_size = .30, 
                                                     random_state = 0) #splits data into testing and learning sections in 70/30 split

KNN = KNeighborsClassifier(n_neighbors = 15).fit(X_train, Y_train)

def accuracy(c, p):
    print('Accuracy of test: ', accuracy_score(c, p))
    print('Confusion matrix data: \n', PD.DataFrame(confusion_matrix(c, p)))
    print('Classifications: \n', classification_report(c, p, digits = 3))

accuracy(Y_Test, KNN.predict(X_Test)) #runs accuracy test on KNN data.

print(Demo)