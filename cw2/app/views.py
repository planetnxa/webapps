from app import app
from flask import render_template, request,session
from sqlalchemy import func
#import db for context purposes, and place databse work in the actual application functions

# initialise these at -1 so when we start we can differentiate between no input, and zero values


@app.route("/") #the url for us to work with
def index(): 
    return render_template("index.html")

@app.route("/portfolio") 
def portfolio(): 
    return render_template("portfolio.html")

@app.route("/book-me") 
def book(): 
        return render_template("book.html")

@app.route("/shop") 
def shop(): 
    return render_template("shop.html")

@app.route("/admin") 
def admin(): 
    return render_template("admin.html")

    # intialise the other balances and values etc
