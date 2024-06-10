from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class BuyForm(FlaskForm):
    #title = StringField('Title', validators=[DataRequired()])
    quant = IntegerField('Copies', validators=[DataRequired()])
    #content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Buy')

