import os
import util
import db
import random
from flask import Flask, json, request, render_template
from flask_cors import CORS
from flask_restful import Api
from resources.user import User
from dotenv import load_dotenv
from googleimages_api import get_image

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


score = 0
game_over = False

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

def get_higher(pair):
    higher = 0
    fin_key = None
    for inds in pair:
        if inds[1] >= higher:
            higher = inds[1]
            fin_key = inds[0]
    return (fin_key, higher)

# Vanilla Flask route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

#@app.route("/move_forward")
#def move_forward():
#    return render_template("celeb.html",)



higher_pers = None
vs_pair = []

@app.route("/move_forward", methods=["GET", "POST"])
def move_forward():
    global score
    global vs_pair
    global higher_pers
    global game_over
    if request.method == "GET":
        new_people = get_rand()
        vs_pair.append((new_people[0][0], new_people[0][1]))
        vs_pair.append((new_people[1][0], new_people[1][1]))
        higher_pers = get_higher(vs_pair)
        image1 = get_image(vs_pair[0][0])
        image2 = get_image(vs_pair[1][0])
        return render_template("celeb.html", person1 = new_people[0][0], person2 = new_people[1][0], followers1 = new_people[0][1], followers2 = new_people[1][1], pers_image_1 = image1, pers_image_2 = image2)
    if request.method == "POST":
        if request.form.get("player1"):
            print(higher_pers[0])
            print(vs_pair)
            if higher_pers[0] == vs_pair[0][0]:
                score+=1
                vs_pair = []
                new_people = get_rand()
                vs_pair.append((new_people[0][0], new_people[0][1]))
                vs_pair.append((new_people[1][0], new_people[1][1]))
                higher_pers = get_higher(vs_pair)
                image1 = get_image(vs_pair[0][0])
                image2 = get_image(vs_pair[1][0])
                return render_template("celeb.html", person1 = new_people[0][0], person2 = new_people[1][0], followers1 = new_people[0][1], followers2 = new_people[1][1], pers_image_1 = image1, pers_image_2 = image2)
            else:
                game_over = True
                vs_pair = []
                higher_pers = None
                score = 0
                return render_template("end.html")
        elif request.form.get("player2"):
            print(higher_pers[0])
            print(vs_pair)
            if higher_pers[0] == vs_pair[1][0]:
                score+=1
                vs_pair = []
                new_people = get_rand()
                vs_pair.append((new_people[0][0], new_people[0][1]))
                vs_pair.append((new_people[1][0], new_people[1][1]))
                higher_pers = get_higher(vs_pair)
                image1 = get_image(vs_pair[0][0])
                image2 = get_image(vs_pair[1][0])
                return render_template("celeb.html", person1 = new_people[0][0], person2 = new_people[1][0], followers1 = new_people[0][1], followers2 = new_people[1][1], pers_image_1 = image1, pers_image_2 = image2)
            else:
                game_over = True
                vs_pair = []
                higher_pers = None
                score = 0
                return render_template("end.html")

@app.route("/about", methods = ["GET"])
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    app.run(debug=True)
