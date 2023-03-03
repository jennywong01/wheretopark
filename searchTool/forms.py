from wtforms import Form, StringField, SelectField


class MapSearchForm(Form):
    # choices = [('Restaurant', 'Restaurant'),
    #            ('Park', 'Park'),
    #            ('Theater', 'Theater')]
    # select = SelectField('Search for destination type:', choices=choices)
    search = StringField('Search for your destination:')
