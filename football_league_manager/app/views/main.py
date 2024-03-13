from flask import Blueprint, render_template, redirect, url_for, flash, request
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

@main.route('/update_league/<int:league_id>', methods=['GET', 'POST'])
def update_league(league_id):
    league = League.query.get_or_404(league_id)
    if request.method == 'POST':
        # Process the submitted form data
        league.name = request.form['name']
        # Update other league fields based on the form data
        db.session.commit()
        flash('League updated successfully.', 'success')
        return redirect(url_for('main.manage_leagues'))
    else:
        # GET request: render the form to edit the league
        return render_template('edit_league.html', league=league)


@main.route('/delete_league/<int:league_id>')
def delete_league(league_id):
    league_to_delete = League.query.get_or_404(league_id)
    db.session.delete(league_to_delete)
    db.session.commit()
    flash('League successfully deleted.', 'success')
    return redirect(url_for('main.manage_leagues'))