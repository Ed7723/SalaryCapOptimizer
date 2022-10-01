from flask import Flask
from flask import render_template
from flask import request
from players import load_players
import json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/team", methods=['Post'])
def create_team():
    return 0

@app.route("/players", methods=["Get"])
def get_players():
    players = load_players()
    return [x.__dict__ for x in players]