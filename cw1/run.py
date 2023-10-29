#this is our start up script...so when this file is ran then it sets up the page

from app import app
if __name__ == "__main__":
    app.run(debug=True)

    #hmm...
    '''
    so is the app module just the folder?
    so when you say from app import app does that mean to pick the whole folder
    and then import everything from the folder

    i am very confused,, also regarding the FLASK_APP export thingy???
    '''