from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap, figure
from bokeh.models import HoverTool
import pandas as pd


def read_data(path):
    df = pd.read_csv(path, converters={'lat1_2': pd.eval, 'lng1_2': pd.eval})
    return df


def my_map():
    df = read_data("../test/flask_test.csv")

    map_options = GMapOptions(lat=47.6062, lng=-122.3321, map_type="roadmap", zoom=11)
    hover = HoverTool(
        tooltips=[
            ('Category', '@PARKING_CATEGORY'),
            ('Side', '@SIDE'),
            ('Unit Desc', '@UNITDESC'),
        ]
    )
    p = gmap("AIzaSyBRHz--MwYpTNPjYTRjAK5yXo-g7yZhDa0",
             map_options,
             width=1000, height=600,
             title="Demo",
             tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    p.multi_line(xs='lng1_2', ys='lat1_2', line_width=1, color='Color', source=source)
    return p
