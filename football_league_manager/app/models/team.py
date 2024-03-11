from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    nickname = db.Column(db.String(128), nullable=True)
    short_name = db.Column(db.String(64), nullable=True)
    date_of_foundation = db.Column(db.Date, nullable=True)
    stadium = db.Column(db.String(128), nullable=True)
    capacity_of_stadium = db.Column(db.Integer, nullable=True)
    owner = db.Column(db.String(128), nullable=True)
    manager = db.Column(db.String(128), nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)  # Assuming a 'League' model exists
    website = db.Column(db.String(128), nullable=True)
    logo = db.Column(db.String(256), nullable=True)

    # Representation method for debugging purposes
    def __repr__(self):
        return '<Team {}>'.format(self.name)
