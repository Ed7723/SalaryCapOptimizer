from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/team", methods=['Post'])
def create_team():
    return 0