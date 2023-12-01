from app import app
from flask import render_template, request,session
from sqlalchemy import func
#import db for context purposes, and place databse work in the actual application functions

# initialise these at -1 so when we start we can differentiate between no input, and zero values


@app.route("/") #the url for us to work with
def index(): #this index function is called when we open up the website
        return render_template("index.html")


    # intialise the other balances and values etc
