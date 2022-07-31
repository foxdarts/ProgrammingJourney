# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 08:51:09 2020

@author: foxsq
"""

import pandas as PD
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix # imports for KNN


Data = open(r"C:\Users\foxsq\OneDrive\Documents\ctu school stuff\Big Data Analytics\diabetic_data.csv") #diabetes data csv
illness = PD.read_csv(Data)


illness.drop(['race', 'gender', 'age', 'weight', 'payer_code', 'medical_specialty',
               'diag_1', 'diag_2', 'diag_3', 'max_glu_serum', 'A1Cresult', 
               'metformin', 'repaglinide', 'glimepiride', 'glipizide', 
               'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 
               'acarbose', 'troglitazone', 'tolazamide', 'insulin', 
               'change', 'readmitted', 'nateglinide', 'chlorpropamide', 
               'acetohexamide', 'miglitol', 'examide', 'citoglipton', 
               'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone', 
               'metformin-rosiglitazone', 'metformin-pioglitazone', 'diabetesMed'], axis = 1, inplace = True) #ignore lists that contain only alphabet characters.
illness.head()

print("data shape: ", illness.shape) #gives csv data shape

X = illness.iloc[:, : -1]
Y = illness.iloc[:, -1]

X_train, X_Test, Y_train, Y_Test = train_test_split(X, Y, test_size = .30, 
                                                     random_state = 0) #splits data into testing and learning sections in 70/30 split

KNN = KNeighborsClassifier(n_neighbors = 15).fit(X_train, Y_train)

def accuracy(c, p):
    print('Accuracy of test: ', accuracy_score(c, p))
    print('Confusion matrix data: \n', PD.DataFrame(confusion_matrix(c, p)))
    print('Classifications: \n', classification_report(c, p, digits = 3))

accuracy(Y_Test, KNN.predict(X_Test)) #runs accuracy test on KNN data.
