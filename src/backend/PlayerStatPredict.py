import sklearn
import numpy
import pandas
from sklearn import linear_model
from datetime import timedelta


#This program predicts the stats of the current star raptor players as of Oct 30, 2019 (using linear regression algorithm)
#This formats all the data so the most recent game is on the right, and last played game is on the left, as well as formatting the data given so it is easier to work with
playerData = pandas.read_csv("vanvleet2021.csv")

playerData = playerData[playerData["MP"].str.contains("Inactive") == False]
playerData = playerData[playerData["MP"].str.contains("Did Not Play") == False]
playerData = playerData[playerData["MP"].str.contains("Did Not Dress") == False]
playerData = playerData[playerData["FT%"].str.contains("NaN") == False]
playerData = playerData[["MP","FG","FGA","FG%","3P","3PA","3P%","FT","FTA","FT%","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS","+/-"]]

def seconder(x):
	mins, secs = map(float, x.split(':'))
	td = timedelta(minutes=mins, seconds=secs)
	return td.total_seconds()
playerData['MP'] = playerData['MP'].apply(seconder)

print(playerData)


PTSpredict = "PTS"
x = numpy.array(playerData.drop([PTSpredict],1))
y = numpy.array(playerData[PTSpredict])


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1 )
linear = linear_model.LinearRegression().fit(x_train, y_train)
predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x],x_test,y_test)
