from app.validates import Unique
from app.models.districtModel import District
from wtforms import Form, StringField, validators, IntegerField


class DistrictRule(Form):
    name = StringField('name', [validators.Length(min=2, max=50), Unique(
        District, District.name, District.id if District.id is not None else None)])
    code = StringField('code', [validators.Length(min=2, max=10), Unique(
        District, District.code, District.id if District.id is not None else None)])
    city_id = IntegerField('city_id', [validators.required()])
