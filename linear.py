import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, model_selection, svm

if(len(sys.argv) < 2) :
	print 'Usage: linear.py <stock name>'
	exit()
else :
	stock = sys.argv[1]
	stock = stock.upper()

forecast_out = int(30)  # predicting 30 days into future

df = pd.read_csv('data.csv')[[stock]]

df['Prediction'] = df[stock].shift(-forecast_out) #  label column with data shifted 30 units up

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

X_forecast = X[-forecast_out:] # set X_forecast equal to last 30
X = X[:-forecast_out] # remove last 30 from X, X is price without last 30 elements

y = np.array(df['Prediction']) 
y = y[:-forecast_out] # y is X shift -30
forecast_expection = y[-forecast_out:]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2)

# Training
clf = LinearRegression()
clf.fit(X_train,y_train)
# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)

forecast_prediction = clf.predict(X_forecast)
print(forecast_prediction)

'''
# Plot Scatter
plt.title('Linear Regression')
plt.scatter(forecast_expection, forecast_prediction)

# Create model
model = LinearRegression(fit_intercept=True)
model.fit(forecast_expection[:, np.newaxis], forecast_prediction)

forecast_min = min(min(forecast_expection), min(forecast_prediction))
forecast_max = max(max(forecast_expection), max(forecast_prediction))

xfit = np.linspace(forecast_min, forecast_max)
yfit = model.predict(xfit[:, np.newaxis])
 
# Plot
plt.plot(xfit, yfit);
plt.xlabel('Expected price')
plt.ylabel('Predicted price')
plt.axis([forecast_min, forecast_max, forecast_min, forecast_max])
plt.grid()
plt.show()
'''
