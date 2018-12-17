from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    code = db.Column(db.String(10), index=True, unique=True)

    district = db.relationship('District', backref='city')

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return ' ' % (self.name)
