from flask import Blueprint, render_template
from app import db
from app import create_app
from app.models.leagues import League

# Create a Blueprint instance
main = Blueprint('main', __name__)

# Define the route for the home page
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/home_admin')
def home_admin():
    return render_template('home_admin.html')

@main.route('/manage_leagues')
def manage_leagues():
    leagues = League.query.all()
    return render_template('manage_leagues.html', leagues=leagues)

@main.route('/edit_league/<int:id>', methods=['GET', 'POST'])
def edit_league(id):
    # Your code to edit the league with the given id
    return render_template('edit_league.html', league_id=id)