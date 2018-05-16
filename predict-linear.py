import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, model_selection, svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

if(len(sys.argv) < 2) :
	print 'Usage: predict-linear.py <stock name>'
	exit()
else :
	stock = sys.argv[1]
	stock = stock.upper()

# Read data
data = pd.read_csv('StocksData/' + stock + '.csv')

# Create model
x = data[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']][:len(data)-1]
last_x = data[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']][len(data)-1:]
y = data['NEXT_OPEN_PRICE'][:len(data)-1]

x_train, x_test, y_train, y_test = train_test_split(x, y,random_state=0)

lr = LinearRegression(fit_intercept=True,)
lr.fit(x_train, y_train)

# Prediction
y_predicted = lr.predict(last_x)
print y_predicted
#print y_predicted
