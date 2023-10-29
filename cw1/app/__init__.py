from flask import Flask

app = Flask(__name__)

from app import views

#this creates a Flask object then imports view type modules to enable visualisation.
#so create a Flask object/ application and name it app
#from the flask application known as app, import the views modules