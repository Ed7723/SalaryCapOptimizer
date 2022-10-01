from flask import Flask,  url_for, render_template, request 
from players import load_players, Player
import json

app = Flask(__name__)

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

@app.route("/table")
def table():
    return render_template('table.html')
