from wtforms import Form, StringField, validators


class CityRule(Form):
    name = StringField('name', [validators.Length(min=2, max=50)])
    code = StringField('code', [validators.Length(min=2, max=10)])
