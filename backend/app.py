import os
import util
import db
import random
from flask import Flask, json, request, render_template
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

people = {"Cristiano Ronaldo" : 'cristiano',
"Lionel Messi": 'leomessi',
"Kylie Jenner": 'kyliejenner',
"Dwayne Johnson": 'therock',
"Ariana Grande": 'arianagrande',
"Selena Gomez": 'selenagomez',
"Kim Kardashian": 'kimkardashian',
"Beyoncé": 'beyonce',
"Justin Bieber": 'justinbieber',
"Kendall Jenner": 'kendalljenner',
"Khloé Kardashian": 'khloekardashian',
"National Geographic": 'natgeo',
"Taylor Swift": 'taylorswift',
"Jennifer Lopez": 'jlo',
"Nike": 'nike',
"Virat Kohli":	'virat.kohli',
"Neymar": 'neymarjr',
"Nicki Minaj":	'nickiminaj',
"Miley Cyrus":	'mileycyrus',
"Kourtney Kardashian":	'kourtneykardash',
"Katy Perry": 'katyperry',
"Kevin Hart": 'kevinhart4real',
"Demi Lovato":	'ddlovato',
"Cardi B":	'iamcardib',
"Rihanna":	'badgalriri',
"Zendaya":	'zendaya',
"Ellen DeGeneres":	'theellenshow',
"Real Madrid CF": 'realmadrid',
"FC Barcelona": 'fcbarcelona',
"LeBron James": 'kingjames',
"Chris Brown": 'chrisbrownofficial',
"Drake": 'champagnepapi',
"Billie Eilish": 'billieeilish',
"UEFA Champions League": 'championsleague',
"Vin Diesel": 'vindiesel',
"Dua Lipa": 'dualipa',
"NASA": 'nasa',
"Gigi Hadid": 'gigihadid',
"Shakira":	'shakira',
"Victoria's Secret": 'victoriassecret',
"Priyanka Chopra": 'priyankachopra',
"David Beckham": 'davidbeckham',
"Shraddha Kapoor":	'shraddhakapoor',
"Gal Gadot": 'gal_gadot',
"Lisa": 'lalalalisa_m',
"Snoop Dogg": 'snoopdogg',	
"Neha Kakkar":	'nehakakkar',
"Shawn Mendes": 'shawnmendes',
"Narendra Modi": 'narendramodi'}

vs_pair = {}

def get_rand():
    try:
        first_person, followers1 = random.choice(list(people.items()))
        del people[first_person]
        sec_person, followers2 = random.choice(list(people.items()))
        del people[sec_person]
        vs_list = ((first_person, followers1), (sec_person, followers2))
        return vs_list
    except:
        return False

# Vanilla Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    score = 0
    game_over = False
    if request.method == "POST":
        if request.form.get("person1"):
            pass
        elif request.form.get("person2"):
            pass
    elif request.method == "GET":
        new_people = get_rand()
        vs_pair[new_people[0][0]] = new_people[0][1]
        vs_pair[new_people[1][0]] = new_people[1][1]
        return render_template("index.html", title='Clout Compare', person1 = new_people[0][0], person2 = new_people[1][0], test = vs_pair)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
