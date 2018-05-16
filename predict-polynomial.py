import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import preprocessing, model_selection, svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

if(len(sys.argv) < 2) :
	print 'Usage: predict-polynomial.py <stock name>'
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

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

classifier = PolynomialFeatures(degree = 3)
X_poly = classifier.fit_transform(x_train)

lr = LinearRegression(fit_intercept=True)
lr.fit(X_poly, y_train)
		
classifier.fit(X_poly, y_train)

# store result from classification
predicted_y = lr.predict(classifier.fit_transform(last_x))
print predicted_y
