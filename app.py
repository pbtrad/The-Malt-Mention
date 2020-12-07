import os
from flask import (
    Flask, url_for, render_template,
     redirect, request, session)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/register")
def register():
    return render_template("register.html")




if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)