from app import db

class makeExp(db.Model):
    # all models must extend the ,Models thing
    # the database is a class, each 
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    desc = db.Column(db.String(400))

    # double for exp and for inc or make a whole 
    def makeExp(self,desc, cost,inc_type):
        self.desc = desc
        self.cost = cost
        self.inc_type = inc_type

class makeInc(db.Model):
    # all models must extend the ,Models thing
    # the database is a class, each 
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    desc = db.Column(db.String(400))

    # double for exp and for inc or make a whole 
    def makeInc(self,desc, cost):
        self.desc = desc
        self.cost = cost
