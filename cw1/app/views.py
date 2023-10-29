from app import app
from flask import render_template 
#not sure why exactly we are importing app to app
# but remember to import the render template thing or you can't imports the sites you designed

@app.route("/") #the url for us to work with
def index(): #not sure if the function name matters here but this is the index page
    return render_template("index.html")

    #oh okay so when we switch to the part of the website known by "/" then the index function is called
    #which then returns the return stuff