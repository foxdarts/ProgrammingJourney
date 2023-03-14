import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


dataframe = pd.read_csv("file locationand name") #change dataframe to be a specific name for this dataframe. change file location and name to be the file you want to read and the file path to find it.

dataframe #this will print the dataframe so you can see the coloums and rows.  will also tell you row count and coloum count


train, test = train_test_split(dataframe, test_size=.2, random_state=1) #splits the data into a randomly selected segment equaling 20 percent of the data to train and the rest to display.

predictors = ["axis 1", "axis 2"] #using headers within the dataframe to pick what will be displayed on the end result
target = "points" #this sets how data points fit within your axis choices

X = train[predictors].copy() #creates a matrix for your axis graph

Y = train[[target]].copy() #creates a matrix for the points on the graph

x_mean = X.mean() #gathers the mean of your x values within the matrix
x_std = X.std() #creates a standard deviation for the values in the x matrix

X = (X - x_mean) / x_std #scales the values in x

X["intercept"] = 1 #adds a value of 1 for each row in the x matrix
X = X[["intercept"] + predictors] #feeds the intercept data into the matrix

X.transpose #turns the x matrix from coloumsXrows to RowsXcoloums

alpha = 2 #we are using this as out lambda function
I = np.identity(X.shape[1]) #should generate a array with 1 in the diagonal from top left to bottom right

I[0][0] = 0 #sets top left value in array to be 0. needed to not invalidate y intercept for dataframe

penalty = alpha * I #generates the penalty matrix for some reason is used to help solve for B

B = np.linalg.inv(X.transpose @ X + penalty) @ X.transpose @ Y #@ used to multiply matrix together. this gives the inverse of the lineary algorithm to be used in our array. then feeds everything into B so we have our linear coefficients and can complete our ridge regression coefficients

B.index = ["y intercept", "axis 1", "axis 2"] # use this to label the yintercept and the axis names within B

#now we start the prediction model usint our training sets

test_X = test[predictors]

test_X = (test_X - x_mean) / x_std #use data from training sets.  you wont always know the testing sets so using the trained data makes this more accurate

test_X["intercept"] = 1 #use same number as training segment for best numbers

test_X = test_X[["intercept"] + predictors] #gives matrix with intercept, axis1, and axis2

predictions = test_X @ B #gives us a set that shows possible values

#compair this linear segment to a ridge segment from sklearn

from sklearn.linear_model import Ridge

ridge = Ridge(alpha = alpha) #sets alpha in ridge to our alpha

ridge.fit(X[predictors], Y) #feads our data into ridge algorythm. intercept isnt used as ridge adds its own automatically

#create graphical representation of data
def ridge_fit(train, predictors, target, alpha): #function for feeding all the code we just wrote into a ridge regression training template
    
    X = train[predictors].copy()
    Y = train[[target]].copy() #tyrains the data
    
    x_mean = X.mean()
    x_std = X.std() #finds mean and standard deviation
    
    X = (X - x_mean) / x_std
    X["intercept"] = 1
    X = X[["intercept"] + predictors] #adds intercept
    
    penalty = alpha * np.idenity(X.shape[1])
    penalty[0][0] = 0 #calculates penalty matrix
    
    B = np.linalg.inv(X.transpose @ X + penalty) @ X.transpose @ Y
    B.index = ["intercept", "axis1", "axis2"]
    return B, x_mean, x_std #returns coefficiants, mean, and std deviation for training data

def ridge_prediction(test, predictors, x_mean, x_std, B): #funtion for using training data against testing data
    
    test_X = test[predictors]
    test_X = (test_X - x_mean) / x_std
    test_X["intercept"] = 1
    test_X = test_X[["intercept"] + predictors]
    
    predictions = test_X @ B
    return predictions

from sklearn.metrics import mean_absolute_error #tells us the difference between actual values and predicted values

errors = [] #empty array to store errors in actual values against predicted values

alphas = [10**i for i in range(-2,4)] #generates alhpa values 0.01, .1, 1, 10, 100, 1000 as a base. can modify these if needed to fit data structure

for alpha in alphas:
    B, x_mean, x_std = ridge_fit(train, predictors, target, alpha) #for loop using training data
    
    predictions = ridge_prediction(test, predictors, x_mean, x_std, B) #testing segment of loop
    
    errors.append(mean_absolute_error(test[target], predictions)) #feeds data into emply errors array
    
errors #prints alpha values. the lowest alpha value in this set gives us the best alpha value to use for our dataset without overweighting or underweighting the data



