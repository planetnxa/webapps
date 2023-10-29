from flask import render_template, flash #flash?????
from app import app
from .forms import CalculatorForm # the name .forms why? full stop wetin?

@app.route('/calc',methods=["GET","POST"]) #so you can take input??
def calc():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash("valid, the answer is %s"%(form.number1.data+form.number2.data))
        # why do the numbers stay on refresh....btw flash refers to quickie message....not the adobe ting

    return render_template('calculator.html',title="calc",form=form)
    #render temp is the function fi make the site in flask based on the given html

@app.route('/')
def index():
    user = {"name":"JAaDE"}
    return render_template("index.html", user=user)
#so is this a view?? 
# displayed in the web browser when the root document is requested from the server
# what is a route and what is a decorator??
# watch an intro vid to flask

#okay so this is the thing that we see when we say run....but i don"t know how the structure works

#is there a reason

@app.route('/fruit') #known as how to access it via the web page
def displayFruit(): #but when did we call this function??? like ever
    fruitsList = ["Apple","banana", "pineapple"]
    return render_template("fruit_inherit.html",title="bratz",fruitss=fruitsList)
    # because you have a function in the html sect ccalled fruitss, you need to define it here 
    # in this python  document, fruits can ya dig it?
