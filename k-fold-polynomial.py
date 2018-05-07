import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import KFold



def import_data(stockName):
	# import total dataset
	data = pd.read_csv('StocksData/' + stockName + '.csv')
	data = data.drop(['DATE'], 1)
	data = data.dropna()

	# get a list of column names
	headers = list(data.columns.values)

	# separate into independent and dependent variables
	x = data[headers[:-1]]
	y = data[headers[-1:]].values.ravel()
	y[y == "UP"] = 1
	y[y == "DRAW"] = 0
	y[y == "DOWN"] = -1

	return x, y

if __name__ == '__main__':
	# get training and testing sets
	stockName = 'ADVANC'
	x, y = import_data(stockName)

	# set to 10 folds
	skf = KFold(n_splits=10)

	# blank lists to store predicted values and actual values
	predicted_y = []
	expected_y = []

	# partition data
	accuracy = 0
	for train_index, test_index in skf.split(x, y):
		# specific ".loc" syntax for working with dataframes
		x_train, x_test = x.loc[train_index], x.loc[test_index]
		y_train, y_test = y[train_index], y[test_index]

		# create and fit classifier
		classifier = PolynomialFeatures(degree = 3)
		X_poly = classifier.fit_transform(x_train)

		lr = LinearRegression()
		lr.fit(X_poly, y_train)
		
		classifier.fit(X_poly, y_train)

		# store result from classification
		predicted_y = lr.predict(classifier.fit_transform(x_test))

		# store expected result for this specific fold
		expected_y = y_test

		# save and print accuracy
		accuracy += np.sqrt(metrics.mean_squared_error(expected_y, predicted_y))


	#accuracy = metrics.accuracy_score(expected_y, predicted_y)
print "Polynomial-regression accuracy with " + stockName + ": " , accuracy/10
