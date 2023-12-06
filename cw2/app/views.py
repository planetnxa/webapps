from app import app
from flask import render_template, request,session
from sqlalchemy import func
#import db for context purposes, and place databse work in the actual application functions

# initialise these at -1 so when we start we can differentiate between no input, and zero values
"""
how to ensure emails and ting
layout

"""

@app.route("/") #the url for us to work with
def index(): 
    return render_template("index.html")

@app.route("/portfolio") 
def portfolio(): 
    return render_template("portfolio.html")

@app.route("/port-abstudio") 
def port_abstudio(): 
    return render_template("port-abstudio.html")

@app.route("/port-corazon") 
def port_corazon(): 
    return render_template("port-corazon.html")

@app.route("/port-miakrylics") 
def port_miaakrylics(): 
    return render_template("port-miakrylics.html")

@app.route("/book-me") 
def book(): 
    return render_template("book.html")

@app.route("/book-conf") 
def book_conf(): 
    return render_template("book-confirmation.html")

@app.route("/shop") 
def shop(): 
    return render_template("shop.html")

@app.route("/admin") 
def admin(): 
    return render_template("admin.html")

@app.route("/admin-view") 
def admin_orders(): 
    return render_template("admin-view.html")

    # intialise the other balances and values etc
