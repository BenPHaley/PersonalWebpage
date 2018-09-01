
# A very simple Flask Hello World app for you to get started with...

#loads the Flask Framework so that you can use it
#added render_template since I am beginning to use it in functions
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#creates a Flask application to run your code on
app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="bhaley7",
    password="FirstSQLDatabase",
    hostname="bhaley7.mysql.pythonanywhere-services.com",
    databasename="bhaley7$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
#servers are closed after 300 seconds of non-use, 299 ensures you have a fresh server
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#each table in the data base can be represented by a class
class Comment (db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

#stores the users of the site. Once they register they will be added
#to the database
# class User (db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(30))
#     last_name = db.Column(db.String(30))
#     username = db.Column(db.String(40))
#     password = db.Column(db.String(40))



#Home page with a login form
@app.route("/", methods=["GET", "POST"])
def home():
   # if request.method = "POST":
    return render_template("home.html")


@app.route("/blog", methods=["GET", "POST"])
def blog():
    if request.method == "POST":
        comment = Comment(content=request.form["contents"])
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('blog'))

    return render_template("main.html", comments=Comment.query.all())

# @app.route("/authorize", method=["GET", "POST"])
# def authorize():
#     error = None
#     if request.method == "POST":
#         if (valid_account(request.form['username'], request.form['password'])):
#             error = "Successful Login"
#             #return login(request.form['username'])
#         else:
#             error = "Invalid username/password"

#     return render_template("home.html", error=error)


# def valid_account(username, password):
#     return True;


