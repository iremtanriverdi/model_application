# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


dataset = pd.read_csv('sur.csv')

# drop null values
dataset.dropna(inplace=True)

X = dataset.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13]] # seleceting covariates from dataset
y = dataset.iloc[:, 14] # seleceting response from dataset



# model 
from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(X, y)
regressor.score(X, y)



# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1, 2, 0,1,0,3,1,0,1,0,0,1,0]]))


