import pandas
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold


def import_data(stockName):
	# import total dataset
	data = pandas.read_csv('StocksData/' + stockName + '.csv')
	data = data.drop(['DATE'], 1)
	data = data.dropna()

	# get a list of column names
	headers = list(data.columns.values)

	# separate into independent and dependent variables
	x = data[headers[:-1]]
	y = data[headers[-1:]].values.ravel()

	return x, y

if __name__ == '__main__':
	# get training and testing sets
	stockName = 'ADVANC'
	x, y = import_data(stockName)

	# set to 10 folds
	skf = StratifiedKFold(n_splits=10)

	# blank lists to store predicted values and actual values
	predicted_y = []
	expected_y = []

	# partition data
	for train_index, test_index in skf.split(x, y):
		# specific ".loc" syntax for working with dataframes
		x_train, x_test = x.loc[train_index], x.loc[test_index]
		y_train, y_test = y[train_index], y[test_index]

		# create and fit classifier
		classifier = GaussianNB()
		classifier.fit(x_train, y_train)

		# store result from classification
		predicted_y.extend(classifier.predict(x_test))

		# store expected result for this specific fold
		expected_y.extend(y_test)

	# save and print accuracy
	accuracy = metrics.accuracy_score(expected_y, predicted_y)
print("GaussianNB accuracy with " + stockName + ": " + accuracy.__str__())
