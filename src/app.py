from flask import Flask,  url_for, render_template, request, redirect
from players import load_players, Player
from PlayerStatPredict import Predict
import json

app = Flask(__name__)

currentPlayerBase = (('Pascal Siakam','Toronto Raptors'),('Fred Vanvleet','Toronto Raptors'),('Gary Trent Jr','Toronto Raptors'),('OG Anunoby','Toronto Raptors'),('Scottie Barnes','Toronto Raptors'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/team", methods=['Post'])
def create_team():
    player_list = json.loads(request.data)
    player_list = [Player(x["name"], x["salary"], x["team"]) for x in player_list]
    return ""

@app.route("/players", methods=["Get"])
def get_players():
    players = load_players()
    return [x.__dict__ for x in players]

@app.route("/pascalsiakam", methods=["Get"])
def get_player_prediction_pascal():
    stats = Predict("backend/siakam2021.csv")
    return render_template('search.html', stats = stats.__dict__)

@app.route("/pascalsiakam", methods=["Get"])
def get_player_prediction_fred():
    stats = Predict("backend/vanvleet2021.csv")
    return render_template('search.html', stats = stats.__dict__)

@app.route("/pascalsiakam", methods=["Get"])
def get_player_prediction_scottie():
    stats = Predict("backend/barnes2021.csv")
    return render_template('search.html', stats = stats.__dict__)

@app.route("/garytrentjr", methods=["Get"])
def get_player_prediction_gary():
    stats = Predict("backend/trentjr2021.csv")
    return render_template('search.html', stats = stats.__dict__)

@app.route("/oganunoby", methods=["Get"])
def get_player_prediction_og():
    stats = Predict("backend/anunoby2021.csv")
    return render_template('search.html', stats = stats.__dict__)

    
@app.route("/table")
def table():
    return render_template('table.html',currentPlayers = currentPlayerBase)

