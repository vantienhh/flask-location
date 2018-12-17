from wtforms import ValidationError


class Unique(object):
    """ validator that checks field uniqueness """

    def __init__(self, model, field, id=None, message=None):
        self.model = model
        self.field = field
        self.id = id
        if not message:
            message = u'this element already exists'
        self.message = message

    def __call__(self, form, field, id=None):
        check = self.model.query.filter(self.field == field.data, id != (
            self.id if self.id is not None else None)).first()
        if check:
            raise ValidationError(self.message)
