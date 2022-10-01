from audioop import avg
from click import prompt
import sklearn
import numpy
import pandas
import sklearn
from sklearn import linear_model
from datetime import timedelta

class PredictionResult:
	def __init__(self, points, rebounds, assists, steals, blocks):
		self.points = points
		self.rebounds = rebounds
		self.assists = assists
		self.steals = steals
		self.blocks = blocks

def seconder(x):  #get seconds for minutes played
	mins, secs = map(float, x.split(':'))
	td = timedelta(minutes=mins, seconds=secs)
	return td.total_seconds()


def Predict(file_path):
	#This program predicts the stats of a given player with their csv file from basketball-reference.com (using linear regression algorithm)

	playerData = pandas.read_csv(file_path) #insert player csv file here, make sure path is correct. 

	playerData = playerData[playerData["MP"].str.contains("Inactive") == False]
	playerData = playerData[playerData["MP"].str.contains("Did Not Play") == False]
	playerData = playerData[playerData["MP"].str.contains("Did Not Dress") == False]
	playerData = playerData[playerData["FT%"].str.contains("NaN") == False]  #need to shift the games played/rnk down


	playerData = playerData[["MP","FGA","TRB","AST","STL","BLK","TOV","PTS","+/-"]]

	playerData['MP'] = playerData['MP'].apply(seconder)  #Take in mind, MP is not minutes played and actually seconds played


	predictionVar = "PTS"

	x = numpy.array(playerData.drop([predictionVar],1))  #creates an array of arrays containing the variables
	y = numpy.array(playerData[predictionVar])           #creates an array of the wanted variable


	x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.05 )  #trains model with 95 percent of data and test on 5% of data


	linear = linear_model.LinearRegression()  #choosing linear regression as all stats are correalated 

	linear.fit(x_train,y_train)  #fit model with the training data


	predictions = linear.predict(x_test)  #predict using x_test, which is randomized by sklearn
	# print("\nGiven that in a certain game, player achieves the following stats: ")
	# print("MP: " + str(x_test[1][0]) + " FGA: "+ str(x_test[1][1]) +  " TRB: " + str(x_test[1][2]))
	# print("AST: " + str(x_test[1][3]) + " STL: " + str(x_test[1][4]) + " BLK:" + str(x_test[1][5]) + " TOV: " + str(x_test[1][6]))
	# print("+/-: " + str(x_test[1][7]) )
	# userGuess=input("What do you think the player's point score is?: ")
	#print("The machine learning model predicted: " + str(predictions[1]))
	#print("The actual point score is: " + y_test[1]) 

	return PredictionResult(str(predictions[1]), str(x_test[1][2]), str(x_test[1][3]), str(x_test[1][4]), str(x_test[1][5]))



#for i in range(len(predictions)):   #uncomment out if you want to see the test data and the predictions for thos
#  print("The predicted output generated is: " + str(predictions[i]) + "The test data used to generate the prediction was: " + str(x_test[i]) + "The actual output was: " + str(y_test[i]))
