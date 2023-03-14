'''
this module plot different parking layer to gmap
'''
import os
import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from bokeh.models import HoverTool
# pylint: disable=import-error
from .config import GOOGLE_API_KEY
from .distance import rec_parking

# pylint: disable=R0914
def my_map(lat, lng, zoom):
    """
    this function takes lat and lng from user input and plot parking spaces nearby
    """
    if lat is None:
        raise ValueError("Latitude is not valid")
    if lng is None:
        raise ValueError("Longitude is not valid")
    if not isinstance(lat, (np.float64, float)):
        raise TypeError("Latitude is not float")
    if not isinstance(lng, (np.float64, float)):
        raise TypeError("Longitude is not float")
    if not isinstance(zoom, int):
        raise TypeError("Zoom is not integer")
    if lat < 47 or lat > 48:
        raise ValueError("Latitude is out of the range of Seattle")
    if lng < -123 or lng > -121:
        raise ValueError("Longiture is out of the range of Seattle")
    if zoom <= 0:
        raise ValueError("Zoom is out of range")

    dirname = os.path.dirname(__file__)
    filename_paid = os.path.join(dirname, 'df_paid.pkl')
    filename_free = os.path.join(dirname, 'df_free.pkl')

    df_paid = pd.read_pickle(filename_paid)
    df_free = pd.read_pickle(filename_free)

    map_options = GMapOptions(lat=lat, lng=lng, map_type="roadmap", zoom=zoom)
    df_rec = rec_parking(lat, lng)

    source1 = ColumnDataSource(data=df_free)
    source2 = ColumnDataSource(data=df_paid)
    source3 = ColumnDataSource(data=df_rec)

    # pylint: disable=invalid-name
    # api_key = os.getenv("GOOGLE_API_KEY", "")
    api_key = GOOGLE_API_KEY
    p = gmap(api_key,
             map_options,
             width=1000, height=600,
             tools=['reset', 'wheel_zoom', 'pan'])

    plot1 = p.multi_line(xs='lngs', ys='lats', line_width=2, color='colors',
                         alpha=0.5, source=source1, legend_group="parking_cat")
    p.add_tools(HoverTool(renderers=[plot1], tooltips=[('Category', '@parking_cat'),
                                                       ('Unit_desc', '@unit_desc')]))

    plot2 = p.multi_line(xs='lngs', ys='lats', line_width=2, color='colors',
                         alpha=0.5, source=source2, legend_group="parking_cat")
    p.add_tools(HoverTool(renderers=[plot2], tooltips=[('Category', '@parking_cat'),
                                                       ('Unit_desc', '@unit_desc'),
                                                       ('ParkingSpaceCount', '@ParkingSpaceCount')
                                                       ]))

    p.multi_line(xs='lngs', ys='lats', line_width=3, color='colors', alpha=1, source=source3)

    p.star_dot(lng, lat, size=25, color='red')

    p.legend.location = "bottom_right"
    p.legend.title = "Legend"
    p.legend.background_fill_alpha = 1
    return p
