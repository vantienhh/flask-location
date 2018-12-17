from app.validates import Unique
from app.models.cityModel import City
from wtforms import Form, StringField, validators


class CityRule(Form):
    name = StringField(
        'name', [validators.Length(min=2, max=50), Unique(City, City.name, City.id if City.id is not None else None)])
    code = StringField('code', [validators.Length(min=2, max=10), Unique(
        City, City.code, City.id if City.id is not None else None)])
