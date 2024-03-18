from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required, login_user,logout_user
from werkzeug.security import check_password_hash
from flask_wtf.csrf import generate_csrf
from app import create_app
from app.models.leagues import League
from app.models.users import User
from app.extensions import db
from app.forms.forms import LeagueForm



# Create a Blueprint instance
main = Blueprint('main', __name__)

# Define the route for the home page
@main.route('/')
def index():
    return render_template('home.html')

@main.route('/home_admin')
@login_required
def home_admin():
    # Make sure only admins can access this page
    if current_user.role != 'admin':
        abort(403)  # Forbidden
    return render_template('home_admin.html')

@main.route('/home_viewer')
@login_required
def home_viewer():
    # Make sure only viewers can access this page
    if current_user.role != 'viewer':
        abort(403)  # Forbidden
    return render_template('home_viewer.html')

@main.route('/manage_leagues')
def manage_leagues():
    leagues = League.query.all()
    return render_template('manage_leagues.html', leagues=leagues)

@main.route('/view_leagues')
def view_leagues():
    leagues = League.query.all()
    return render_template('view_leagues.html', leagues=leagues)

@main.route('/delete_league/<int:league_id>')
def delete_league(league_id):
    league_to_delete = League.query.get_or_404(league_id)
    db.session.delete(league_to_delete)
    db.session.commit()
    flash('League successfully deleted.', 'success')
    return redirect(url_for('main.manage_leagues'))


@main.route('/create_league', methods=['GET', 'POST'])
def create_league():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        country = request.form.get('country')
        date_of_foundation = request.form.get('date_of_foundation')
        number_of_teams = request.form.get('number_of_teams')
        level_on_pyramid = request.form.get('level_on_pyramid')
        current_champion = request.form.get('current_champion')
        most_champions = request.form.get('most_champions')
        most_appearances = request.form.get('most_appearances')
        top_scorer = request.form.get('top_scorer')
        logo = request.form.get('logo')
               
        # Create a new League instance
        new_league = League(name=name, country=country, date_of_foundation=date_of_foundation, number_of_teams=number_of_teams,
                            level_on_pyramid=level_on_pyramid, current_champion=current_champion, most_champions=most_champions,
                            most_appearances=most_appearances, top_scorer=top_scorer, logo=logo)  # Add more fields accordingly
        
        # Add to the database
        db.session.add(new_league)
        db.session.commit()
        
        flash('League successfully created!', 'success')
        return redirect(url_for('main.manage_leagues'))  # Adjust this if you have a different view for the leagues list

    # GET request: just render the template
    return render_template('create_league.html')

@main.route('/update_league/<int:league_id>', methods=['GET', 'POST'])
def update_league(league_id):
    league_to_update = League.query.get_or_404(league_id)
    form = LeagueForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # Update league with form data
            league_to_update.name = form.name.data
            league_to_update.country = form.country.data
            league_to_update.number_of_teams = form.number_of_teams.data
            league_to_update.date_of_foundation = form.date_of_foundation.data
            league_to_update.level_on_pyramid = form.level_on_pyramid.data
            league_to_update.current_champion = form.current_champion.data
            league_to_update.most_champions = form.most_champions.data
            league_to_update.most_appearances = form.most_appearances.data
            league_to_update.top_scorer = form.top_scorer.data
            league_to_update.logo = form.logo.data

            db.session.commit()
            flash('League successfully updated.', 'success')
            return redirect(url_for('main.manage_leagues'))
        else:
            flash('Error updating league. Please check your input.', 'danger')
    elif request.method == 'GET':
        # Pre-populate form with existing league data
        form.name.data = league_to_update.name
        form.country.data = league_to_update.country
        form.number_of_teams.data = league_to_update.number_of_teams
        form.date_of_foundation.data = league_to_update.date_of_foundation
        form.level_on_pyramid.data = league_to_update.level_on_pyramid
        form.current_champion.data = league_to_update.current_champion
        form.most_champions.data = league_to_update.most_champions
        form.most_appearances.data = league_to_update.most_appearances
        form.top_scorer.data = league_to_update.top_scorer
        form.logo.data = league_to_update.logo

    return render_template('edit_league.html', form=form, league=league_to_update)


@main.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        abort(403)  # Forbidden access
    return render_template('home_admin.html')