# -*- coding: utf-8 -*-
"""project-breast cancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17m1RrnMkH05CuRkEMjYr1i9t9p_5JS3g
"""

import csv 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df=sklearn.datasets.load_breast_cancer()

df

data_frame=pd.DataFrame(df.data,columns=df.feature_names)

data_frame.head()

data_frame["label"]=df.target

data_frame.tail()

data_frame.shape

data_frame.info()

data_frame.isnull().sum()

data_frame.describe()

data_frame["label"].value_counts()

"""1-----> benign
0----->malignant

"""

data_frame.groupby("label").mean()

x=data_frame.drop(columns="label",axis=1)
y=data_frame["label"]

print(x)

print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

print(x.shape,x_train.shape,x_test.shape)

model=LogisticRegression()

model.fit(x_train,y_train)

x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(y_train,x_train_prediction)

print("accuracy on training data= ",training_data_accuracy)

x_test_prediction=model.predict(x_test)
test_data_accuracy=accuracy_score(y_test,x_test_prediction)

print("accuracy on test data= ",test_data_accuracy)

input_data=(12.45,15.7,82.57,477.1,0.1278,0.17,0.1578,0.08089,0.2087,0.07613,0.3345,0.8902,2.217,27.19,0.00751,0.03345,0.03672,0.01137,0.02165,0.005082,15.47,23.75,103.4,741.6,0.1791,0.5249,0.5355,0.1741,0.3985,0.1244)

input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print("The breast cancer is malignant")
else:
  print("The breast cancer is benign")

