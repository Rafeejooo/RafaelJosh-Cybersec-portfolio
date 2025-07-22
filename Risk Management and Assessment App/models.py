from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    criticality = db.Column(db.Integer, nullable=False)  

class Vulnerability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    description = db.Column(db.String(200))
    severity = db.Column(db.Integer)  

class Threat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    misp_event_id = db.Column(db.String(50))
    description = db.Column(db.String(200))
    type = db.Column(db.String(50))

class Risk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    threat_id = db.Column(db.Integer, db.ForeignKey('threat.id'))
    likelihood = db.Column(db.Float)  
    impact = db.Column(db.Float)      
    risk_score = db.Column(db.Float) 