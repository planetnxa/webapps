from app import app
from flask import render_template
#not sure why exactly we are importing app to app
# but remember to import the render template thing or you can't imports the sites you designed
g = 1000
i = 100
e = 10

@app.route("/") #the url for us to work with
def index(): #not sure if the function name matters here but this is the index page
    
   gd = g-(i-e)
   return render_template("index.html",incVal=i,goalVal=g,expVal=e, goalDiff=gd)

    #oh okay so when we switch to the part of the website known by "/" then the index function is called
    #which then returns the return stuff

@app.route("/income") 
def income():
    return render_template("income.html")

@app.route("/goal") 
def goal():
    return render_template("goal.html", goalVal=g)

@app.route("/expenditure") 
def exp():
    return render_template("expenses.html")