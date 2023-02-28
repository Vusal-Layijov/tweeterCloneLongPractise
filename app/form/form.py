from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired, Length, URL

class CreateTweet(FlaskForm):
    author=StringField('author', validators=[DataRequired()])
    tweet=StringField('tweet', validators=[DataRequired()])
    submit=SubmitField('Create Tweet')
