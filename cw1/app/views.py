from app import app, models, db
from flask import render_template, request,session
from sqlalchemy import func
#import db for context purposes, and place databse work in the actual application functions

# initialise these at -1 so when we start we can differentiate between no input, and zero values
gval = -1
incomeTotal = -1
expenseVal = -1
balance = 0

@app.route("/") #the url for us to work with
def index(): #this index function is called when we open up the website
    
    # look at the session/storage part 
    #if there is a value called gval in there load it up
    # otherwise initialise it now
    
    if "gval" in session:
        gval= session["gval"]
    else:
        gval = -1
    
    if "incomeTotal" in session:
        incomeTotal= session["incomeTotal"]
    else:
        incomeTotal = 0

    if "expenseVal" in session:
        expenseVal= session["expenseVal"]
    else:
        expenseVal = 0

    # intialise the other balances and values etc
    balance = incomeTotal-expenseVal
    gdiff = int(gval)-(balance)
    return render_template("index.html",incVal=incomeTotal,goalVal=int(gval),expVal=expenseVal, goalDiff=gdiff, balance = balance)

    
# fun fact python arrays have no fixed length!

@app.route("/addval", methods=["POST","GET"]) 
def addval():
    if request.method== "POST":
        
        #initialise the values for record/object for the database given the input user info
        newCostName = request.form["cost_type"]
        newCostVal = request.form["cost_val"]
        costType = request.form["inc_exp"]

        
        #have to add db add  and commit later
        if costType == "exp":
            newCost = models.makeExp(desc = newCostName,cost = newCostVal)
        
            db.session.add(newCost) #this could be simplified because why is it here twice
            db.session.commit()

            expenseVal = db.session.query(func.sum(models.makeExp.cost)).scalar()
            session["expenseVal"]=expenseVal
            return render_template("expenses.html", entries=models.makeExp.query.all())

            #essentially we've added the cost to the respective database
            # then opened the webpage with that databaseso you can see it 
            # in this case it's for expenses
            
        else:
            newCost = models.makeInc(desc = newCostName,cost = newCostVal)
        
            db.session.add(newCost)
            db.session.commit()

            # the scalar() is very important!!
            # return the value of the sum from this function and make it scalar so you can actually use it
            incomeTotal = db.session.query(func.sum(models.makeInc.cost)).scalar()
            session["incomeTotal"]=incomeTotal

            return render_template("income.html", entries=models.makeInc.query.all())
    else:
        # if we are not receiving data here, so we refresh the page, then just reload the page
        return render_template("addvalue.html")



@app.route("/goal", methods=["POST","GET"]) 
def goal():

    #once again check the session....there's an issue with app.context apparently
    if "gval" in session:
        gval= session["gval"]
    else:
        gval = -1

    # to delete the goal, make it -1 so it doesn't register as false/0
    # store it in the session again
    if request.method== "POST":
        gval = -1
        session["gval"]=gval
    return render_template("goal.html", goalVal=int(gval))


@app.route("/editgoal", methods=["POST","GET"])
def newgoal():
    if request.method== "POST":
        gval = request.form["new_goal"]
        session["gval"]=gval

        return render_template("goal.html",goalVal=int(gval) )
    else:
        return render_template("newgoal.html")
        
@app.route("/expenditure") 
def exp():
    return render_template("expenses.html",entries=models.makeExp.query.all())

@app.route("/income") 
def income():
    return render_template("income.html", entries=models.makeInc.query.all())
