from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates/index.html")

@app.routh("/register")
def register():
    