# Logistic Regression: SUV Purchase Data

This dataset reveals information on whether an SUV is purchased or not. The goal is to create a logistic regression model and evaluate if the model corectly predicts the purchase of an SUV by an individual.


#import essential libraries

#Basics
import pandas as pd
import numpy as np

#Visualization
import matplotlib.pyplot as plot
import seaborn as sns
import matplotlib.pyplot as plt

#SKLearn ML
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, classification_report, recall_score
from sklearn.preprocessing import StandardScaler


#import the dataset
suv_data = pd.read_csv('suv_data.csv')


#display the data
suv_data


Exploratory Data Analysis

#Check the number of columns and rows
print(suv_data.shape)

#summarize the data
print(suv_data.describe())

print(suv_data.info())

#view datatypes
print(suv_data.dtypes)

#view first 5 rows
print(suv_data.head())

Visualize the data to access the distribution of the variables.

#plot histogram 
plt.hist(suv_data["Age"], bins = 50)
plt.show()

The histogram shows that age is normally distributed

sns.catplot(x= "Purchased", data = suv_data, hue = "Gender", kind = "count")
plt.show()

The countplot shows that more females bought SUVs than males


# Feature Engineering
logistic regression cannot interpret string data. Therefore, the Gender column will be One-hot coded. One-hot coding converts categorical variables into a binary representation where each category becomes a binary feature column.

Gender_dummy = pd.get_dummies(suv_data["Gender"])

#combine the new dummy dataframe to the original one
suv_data_eng = pd.concat([suv_data, Gender_dummy], axis = 1)
suv_data_eng

#drop categorical columns
suv_df=suv_data_eng.drop("Gender", axis = 1)
suv_df

# Defining the Input(independent) variables and the Target(dependent) variable



Fitting the Logistic Regression model using scikit learn library

#Separate the dataset into input and target variables
y_target = suv_df.Purchased
x_inputs = suv_df[["User ID", "Age", "EstimatedSalary", "Female", "Male"]]

Sklearn will be used to split the data into training and testing data. The training division is to assess how well the data performs. The testing division is to evaluate how well the data performs on data it has not seen before. 

x_train, x_test, y_train, y_test = train_test_split(x_inputs, y_target, train_size=0.8, random_state=50)

print("x_train: ", x_train.shape)
print("x_test: " , x_test.shape)
print("y_train: ", len(y_train))
print("y_test :", len(y_test))

# Scaling the data.
Before the data is fitted, it will be scaled with Standardization (Z-score normalization) method in SKlearn. This method transforms the data to have mean of 0 and a standard deviation of 1. It also rescales the data by subtracting the mean and dividing by the standard deviation.

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

print("x_train: ", x_train)
print("x_test : ", x_test)

# Fitting the model

#Declare a logistic regression classifier

classifier = LogisticRegression(max_iter=1000)
classifier.fit(x_train, y_train)

Measure the accuracy performance of the train data

classifier.score(x_train, y_train)

EXPLAIN DIFF: The score here evaluates the performance of the model, by default, the classifier uses Accuracy as the score. It is the ratio of number of correct predictions to the total number of predictions. It is essentially the fraction of predictions the model got right. It works well with a balanced class, hence, it is essential to have a quick look at the distribution of the class as done above. 

These four outcomes can also be depicted in the form of a confusion matrix, which is nothing but a visual representation of how many times these outcomes occured for our model's predictions.

#  Evaluating the model and Confusion Matrix

preds = classifier.predict(x_test)
preds

con_mat = confusion_matrix(y_test, preds)
con_mat

tn = con_mat[0][0]
fp = con_mat[0][1]
fn = con_mat[1][0]
tp = con_mat[1][1]

print("True Negatives (Correct Non-Purchase): ", tn)
print("False Positives (Incorrect Purchase): ", fp)
print("False Negatives (Incorrect Non-Purchase): ", fn)
print("True Positives (Correct Purchase)", tp)

#Plot the confusion matrix

ConfusionMatrixDisplay.from_estimator(classifier,x_test, y_test)
plt.show()

report = classification_report (y_test, preds)
print (report)

The report clearly shows the model is correctly predicting the dataset.

