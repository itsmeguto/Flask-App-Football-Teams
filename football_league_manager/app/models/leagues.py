from app import db

class League(db.Model):
    __tablename__ = 'leagues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    date_of_foundation = db.Column(db.Date)  # Assuming YYYY-MM-DD format
    number_of_teams = db.Column(db.Integer)
    level_on_pyramid = db.Column(db.Integer)
    current_champion = db.Column(db.String(128))
    most_champions = db.Column(db.String(128))
    most_appearances = db.Column(db.String(128))
    top_scorer = db.Column(db.String(128))
    logo = db.Column(db.String(256))  # Assuming this will be a path to an image

    def __repr__(self):
        return f'<League {self.name}>'