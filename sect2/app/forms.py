from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    number1 = IntegerField("num 1", validators=[DataRequired()])
    number2 = IntegerField("num 2", validators=[DataRequired()])
    
    #why does it have increment arrows?

# two fields for numbers here
# extension of the form layout