import os
from flask import (
    Flask, url_for, render_template,
    redirect, request, session, flash)
from datetime import datetime
import time
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    posts = mongo.db.posts.find()
    return render_template("home.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session users username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "POST":
        post = {
            "post_title": request.form.get("post_title"),
            "post_author": session["user"],
            "post_content": request.form.get("post_content"),
            #"date_posted": request.form.get("date_posted")
            "date_posted": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
        mongo.db.posts.insert_one(post)
        flash("Blog Successfully Added")
        return redirect(url_for("home"))
    blogs = mongo.db.post_content.find().sort("post_content")
    return render_template("blog.html", blog=blog)


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        submit_edit = {
            "post_title": request.form.get("post_title"),
            "post_author": session["user"],
            "post_content": request.form.get("post_content"),
            "date_posted": request.form.get("date_posted")
        }
        
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit_edit)
        flash("Blog Successfully Updated")
        
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("edit_post.html", post=post, blog=blog)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
