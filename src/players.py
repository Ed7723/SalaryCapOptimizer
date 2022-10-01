import csv
filename = "backend/salariesNBA.csv"

class Player:
    def __init__(self, name, team, salary):
        self.name = name
        self.team = team
        self.salary = salary

def load_players():
    players = []
    with open(filename, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            players.append(Player(row[0], row[1], row[2]))
    return players
