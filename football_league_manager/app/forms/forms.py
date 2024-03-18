from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

class LeagueForm(FlaskForm):
    name = StringField('League Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    date_of_foundation = DateField('Date of Foundation', format='%Y-%m-%d', validators=[DataRequired()])
    number_of_teams = IntegerField('Number of Teams', validators=[DataRequired()])
    level_on_pyramid = StringField('Level on Pyramid', validators=[DataRequired()])
    current_champion = StringField('Current Champion', validators=[DataRequired()])
    most_champions = StringField('Most Champions', validators=[DataRequired()])
    most_appearances = StringField('Most Appearances', validators=[DataRequired()])
    top_scorer = StringField('Top Scorer', validators=[DataRequired()])
    logo = StringField('League Logo Path', validators=[DataRequired()])
