import os
import util
import db
import random
from flask import Flask, json, request
from flask_cors import CORS
from flask_restful import Api
from resources.user import User
from dotenv import load_dotenv

# Load Environment variables
load_dotenv()

app = Flask(__name__)
# Allow cross domain apps to access API
CORS(app)

api = Api(app)

people = {"Cristiano Ronaldo" : 368,
"Lionel Messi": 283,
"Kylie Jenner": 282,
"Dwayne Johnson": 279,
"Ariana Grande": 276,
"Selena Gomez": 273,
"Kim Kardashian": 264,
"Beyoncé": 219,
"Justin Bieber": 203,
"Kendall Jenner": 200,
"Khloé Kardashian": 197,
"National Geographic": 192,
"Taylor Swift": 185,
"Jennifer Lopez": 182,
"Nike": 181,
"Virat Kohli":	167,
"Neymar": 165,
"Nicki Minaj":	162,
"Miley Cyrus":	152,
"Kourtney Kardashian":	150,
"Katy Perry": 141,
"Kevin Hart": 128,
"Demi Lovato":	118,
"Cardi B":	114,
"Rihanna":	111,
"Zendaya":	110,
"Ellen DeGeneres":	110,
"Real Madrid CF": 106,
"FC Barcelona": 102,
"LeBron James": 102,
"Chris Brown": 96,
"Drake": 96,
"Billie Eilish": 95,
"UEFA Champions League": 82,
"Vin Diesel": 76,
"Dua Lipa": 75,
"NASA": 71,
"Gigi Hadid": 71,
"Shakira":	71,
"Victoria's Secret": 70,
"Priyanka Chopra":	70,
"David Beckham": 69,
"Shraddha Kapoor":	67,
"Gal Gadot": 67,
"Lisa": 66,
"Snoop Dogg": 65,	
"Neha Kakkar":	64,
"Shawn Mendes": 64,
"Narendra Modi": 62}

# Vanilla Flask route
@app.route("/", methods=["GET"])
def index():
    return "Welcome to my ZotHacks 2020 project!"

@app.route("/game", methods=["GET"])
def game():
    score = 0
    first_person, followers1 = random.choice(list(people.items()))
    del people[first_person]
    sec_person, followers2 = random.choice(list(people.items()))
    del people[sec_person]
    vs_list = ((first_person, followers1), (sec_person, followers2))
    return f"{first_person} and {sec_person}"


if __name__ == "__main__":
    app.run(debug=True)
