from application import db


class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(30), nullable=False)
    player_position= db.Column(db.String(3), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"), nullable=True)
    #teams = db.relationship('Teams', backref='player')

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    players = db.relationship('Players', backref='team')