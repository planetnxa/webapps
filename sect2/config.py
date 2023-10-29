WTF_CSRF_ENABLED = True
SECRET_KEY = "shhh"

import os
basedir = (os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "app.db")
SQLALCHEMY_TRACK_MODIFICATIONS=True
