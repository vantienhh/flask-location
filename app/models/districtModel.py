from app import db


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    code = db.Column(db.String(10), index=True, unique=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    City = db.relationship('City', back_populates="district")

    def __init__(self, name, code, city_id):
        self.name = name
        self.code = code
        self.city_id = city_id

    def __repr__(self):
        return ' ' % (self.name)
