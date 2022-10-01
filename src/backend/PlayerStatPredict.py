from audioop import avg
from click import prompt
import sklearn
import numpy
import pandas
import sklearn
from sklearn import linear_model
from datetime import timedelta



#This program predicts the stats of a given player with their csv file from basketball-reference.com (using linear regression algorithm)

playerData = pandas.read_csv("vanvleet2021.csv")

playerData = playerData[playerData["MP"].str.contains("Inactive") == False]
playerData = playerData[playerData["MP"].str.contains("Did Not Play") == False]
playerData = playerData[playerData["MP"].str.contains("Did Not Dress") == False]
playerData = playerData[playerData["FT%"].str.contains("NaN") == False]  #need to shift the games played/rnk down

playerData = playerData[["MP","FG","FGA","3P","3PA","FT","FTA","TRB","AST","STL","BLK","TOV","PTS","+/-"]]

def seconder(x):  #get seconds for minutes played
	mins, secs = map(float, x.split(':'))
	td = timedelta(minutes=mins, seconds=secs)
	return td.total_seconds()
playerData['MP'] = playerData['MP'].apply(seconder)  #Take in mind, MP is not minutes played and actually seconds played


predictionVar = "PTS"

x = numpy.array(playerData.drop([predictionVar],1))  #creates an array of arrays containing the variables
y = numpy.array(playerData[predictionVar])           #creates an array of the wanted variable


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1 )  #trains model with 90 percent of data and test on 10% of data


linear = linear_model.LinearRegression()  #choosing linear regression as all stats are correalated 

linear.fit(x_train,y_train)  #fit model with the training data
accu = linear.score(x_test,y_test)  # used to print accuracy score
print("The accuracy is: "+ str(accu))
print(x_test[1])
print(x_test[1][1])


predictions = linear.predict(x_test)  #predict using x_test, which is randomized by sklearn
print("\n Given that in a certain game, player achieves the following stats: ")
print("MP: " + str(x_test[1][0]) + " FG: " + str(x_test[1][1]) + " FGA:" + str(x_test[1][2]) + " 3P: " + str(x_test[1][3]) + " 3PA: " + str(x_test[1][4]))
print("FT: " + str(x_test[1][5]) + " FTA: " + str(x_test[1][6]) + " TRB: " + str(x_test[1][7]))
print("AST: " + str(x_test[1][8]) + " STL: " + str(x_test[1][9]) + " BLK:" + str(x_test[1][10]) + " TOV: " + str(x_test[1][11]))
print("+/-: " + str(x_test[1][12]) )
userGuess=input("What do you think the player's point score is?: ")
print("The machine learning model predicted: " + str(predictions[1]))
print("The actual point score is: " + y_test[1])

#for i in range(len(predictions)):
#  print(predictions[i],x_test[i],y_test[i])
