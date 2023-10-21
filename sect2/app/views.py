from flask import render_template
from app import app

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

@app.route('/') #known as how to access it via the web page
def displayFruit():
    fruits = ["Apple","banana", "pineapple"]
    return render_template("fruit.html",fruitss=fruits)
    # because you have a function in the html sect ccalled fruitss, you need to define it here 
    # in this python  document, fruits can ya dig it?
