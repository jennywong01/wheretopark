from wtforms import Form, StringField, SelectField


class MapSearchForm(Form):
    search = StringField('Search for your destination:')
