from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from app.models.users import User
#from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:
    #    return redirect(url_for('main.index'))  # Adjust if needed
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Login successful.', 'success')
            
            # Check user role and redirect accordingly
            if user.role == 'admin':
                return redirect(url_for('main.home_admin'))
                
            elif user.role == 'viewer':
                return redirect(url_for('main.home_viewer'))
                
            else:
                # Handle other roles or undefined role
                flash('Login unsuccessful, please check your registered role.', 'error')
                return redirect(url_for('main.index'))

        else:
            flash('Invalid username or password.','error')
            
    return render_template('login.html')

@auth.route('/logout', methods=["POST"])
def logout():
    logout_user()
    flash('You have been successfully logged out.')
    return redirect(url_for('main.index'))  # Adjust if needed
