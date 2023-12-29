from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
