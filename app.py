from flask import Flask, render_template, request, jsonify, make_response
import pyrebase

from getpass import getpass
import json

from accountHandling import createAccount, loginAccount

with open("db_creds.json") as f:
	firebaseConfig = json.load(f)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/register")
def register():
    return render_template("/register.html")

@app.route('/api/register', methods=["POST"])
def actionRegister():
    data = request.form
    email = data["email"]
    password = data["password"]
    firstName = data["firstName"]
    lastName = data["lastName"]
    bio = data["bio"]
    skills= data["skills"]
    print("skills: ", skills)
    createAccount(db, auth, email, password, firstName, lastName, bio, skills)
    return "penis"

@app.route("/login")
def login():
    return render_template("/login.html")

def setCookie(key, value):
    resp = make_response("Setting cookie")
    resp.set_cookie(key, value)
    return resp

@app.route("/api/login", methods=["POST"])
def actionLogin():
    data = request.form
    email = data["email"]
    password = data["password"]
    uid = loginAccount(db, auth, email, password)

    resp = make_response(render_template("index.html"))
    resp.set_cookie("uid", uid)
    return resp


@app.route("/get")
def getcookie():
    return ""

app.run()