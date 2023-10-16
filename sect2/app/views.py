from app import app

@app.route('/')
def index():
    return "wag1!"
#so is this a view?? 
# displayed in the web browser when the root document is requested from the server
# what is a route and what is a decorator??
# watch an intro vid to flask
