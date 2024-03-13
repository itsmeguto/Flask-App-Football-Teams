# test_db_connection.py

from app import create_app, db

app = create_app()
# We push an application context to tie our database operations to our app
with app.app_context():
    try:
        # Connect to the database and execute a test query
        with db.engine.connect() as connection:
            result = connection.execute(db.text('SHOW TABLES;'))
            tables = [row[0] for row in result]
            print("Connection successful. Found tables:", tables)
    except Exception as e:
        print("Database connection failed:", e)