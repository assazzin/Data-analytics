import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing, model_selection, svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

if(len(sys.argv) < 2) :
	print 'Usage: predict-gaussian.py <stock name>'
	exit()
else :
	stock = sys.argv[1]
	stock = stock.upper()

# Read data
data = pd.read_csv('StocksData/' + stock + '.csv')

# Create model
x = data[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']][:len(data)-1]
last_x = data[['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']][len(data)-1:]
y = data['NEXT_OPEN'][:len(data)-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)


classifier = GaussianNB()
classifier.fit(x_train, y_train)

# store result from classification
predicted_y = classifier.predict(last_x)
print predicted_y
