"""
This module contains a form for searching for a location on a map.
"""

from wtforms import Form, StringField

class MapSearchForm(Form):
    """
    This form allows users to search for a location on a map.
    """
    # pylint: disable=R0903
    search = StringField('Search for your destination:')
