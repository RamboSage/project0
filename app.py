from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/managers")
def managers():
    return render_template("football_managers.html")

@app.route("/players")
def players():
    return render_template("football_players.html")

@app.route("/teams")
def teams():
    return render_template("football_teams.html")
