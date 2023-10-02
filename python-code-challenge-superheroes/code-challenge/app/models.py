from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(50), nullable=False)
    hero_powers = db.relationship("HeroPower", backref="hero")


class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    hero_powers = db.relationship("HeroPower", backref="power")

    @validates("description")
    def validate_description(self, key, description):
        assert len(description) >= 20, "Description must be at least 20 characters long"
        return description

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey("power.id"), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)

    @validates("strength")
    def validate_strength(self, key, strength):
        assert strength in ["Strong", "Weak", "Average"], "Invalid strength value"
        return strength            