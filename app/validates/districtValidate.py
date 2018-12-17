from wtforms import Form, StringField, validators, IntegerField


class DistrictRule(Form):
    name = StringField('name', [validators.Length(min=2, max=50)])
    code = StringField('code', [validators.Length(min=2, max=10)])
    city_id = IntegerField('city_id', [validators.required()])
