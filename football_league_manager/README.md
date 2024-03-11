# Flask-App-Football-Teams

- Python application with Flask that will be connected to a MySQL database via sqlalchemy.
- We will have, in the future, login and authorization for viewers and editors (user profiles)
- Our system will be used to manage football leagues and teams;
- The teams will have the following information:
-- name, nickname, short name, date of foundation, stadium, capacity of stadium, owner, manager, league, website, logo;
- The leagues will have the following information:
-- name, country, date of foundation, number of teams, level on pyramid, current_champion, most_champions, most_appearances, top_scoarer, logo;
- Our architecture will be Model View Controller and Services;

For now, let me understand what a great directory organization would look like

# Notes:
- Important to create venv
    - Root project folder - execute following cmd:
        - source .venv/bin/activate
    - requirements.txt (root)
        - pip3 install -r ./requirements.txt
- Issue could be related to environment so we decided to write into parquet type;

- admin mysql: root / admin1234.

/*** 

/football_league_manager
    /app
        /static
            /css
            /js
            /images
        /templates
            /league
            /team
            /auth
        /models
            __init__.py
            league.py
            team.py
            user.py
        /views
            __init__.py
            league_view.py
            team_view.py
            auth_view.py
        /services
            __init__.py
            league_service.py
            team_service.py
            auth_service.py
        /controllers
            __init__.py
            league_controller.py
            team_controller.py
            auth_controller.py
        /forms
            __init__.py
            league_forms.py
            team_forms.py
            auth_forms.py
        __init__.py
    /migrations
    /instance
        config.py
    /tests
        __init__.py
        test_league.py
        test_team.py
        test_auth.py
    run.py
    config.py
    requirements.txt
