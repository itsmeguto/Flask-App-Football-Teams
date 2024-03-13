from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required, login_user,logout_user
from app import db
from app import create_app
from app.models.leagues import League
from app.models.users import Users
from werkzeug.security import check_password_hash
from flask_wtf.csrf import generate_csrf


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


@main.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        abort(403)  # Forbidden access
    return render_template('home_admin.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if user.role == "admin":
                return redirect(url_for('main.home_admin'))  # Or wherever you want to redirect after login
            else:
                return redirect(url_for('main.home'))  # Or wherever you want to redirect after login
        else:
            flash('Invalid username or password.')

    # If GET request or login failed
    return render_template('index', csrf_token=generate_csrf())  # Render the home page again if login failed



@main.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
