'''
this module plot different parking layer to gmap
'''
import os
import pandas as pd
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from bokeh.models import HoverTool
# pylint: disable=import-error
from distance import rec_parking

# pylint: disable=R0914
def my_map(lat, lng, zoom):
    '''
    this function takes lat and lng from user input and plot parking spaces nearby
    '''
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
    p = gmap("AIzaSyBRHz--MwYpTNPjYTRjAK5yXo-g7yZhDa0",
             map_options,
             width=1000, height=600,
             title="Demo",
             tools=['reset', 'wheel_zoom', 'pan'])

    plot1 = p.multi_line(xs='lngs', ys='lats', line_width=2, color='colors',
                         alpha=0.3, source=source1)
    p.add_tools(HoverTool(renderers=[plot1], tooltips=[('Category', '@parking_cat'),
                                                       ('Unit_desc', '@unit_desc')]))

    plot2 = p.multi_line(xs='lngs', ys='lats', line_width=2, color='colors',
                         alpha=0.3, source=source2)
    p.add_tools(HoverTool(renderers=[plot2], tooltips=[('Category', '@parking_cat'),
                                                       ('Unit_desc', '@unit_desc'),
                                                       ('ParkingSpaceCount', '@ParkingSpaceCount')
                                                       ]))

    p.multi_line(xs='lngs', ys='lats', line_width=3, color='colors', alpha=1, source=source3)

    p.star_dot(lng, lat, size=25, color='red')
    return p
