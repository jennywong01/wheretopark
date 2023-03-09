from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap, figure
from bokeh.models import HoverTool
import pandas as pd


def my_map(lat, lng, zoom):
    df_paid = pd.read_pickle("./searchTool/df_paid.pkl")
    df_free = pd.read_pickle("./searchTool/df_free.pkl")

    map_options = GMapOptions(lat=lat, lng=lng, map_type="roadmap", zoom=zoom)

    source1 = ColumnDataSource(data=df_free)
    source2 = ColumnDataSource(data=df_paid)

    p = gmap("AIzaSyBRHz--MwYpTNPjYTRjAK5yXo-g7yZhDa0",
             map_options,
             width=1000, height=600,
             title="Demo",
             tools=['reset', 'wheel_zoom', 'pan'])

    plot1 = p.multi_line(xs='lngs', ys='lats', line_width=2, color='colors', source=source1)
    p.add_tools(HoverTool(renderers=[plot1], tooltips=[('Category', '@parking_cat'), ('Unit_desc', '@unit_desc')]))

    plot2 = p.multi_line(xs='lngs', ys='lats', line_width=2, color='colors', source=source2)
    p.add_tools(HoverTool(renderers=[plot2], tooltips=[('Category', '@parking_cat'), ('Unit_desc', '@unit_desc'),
                                                       ('ParkingSpaceCount', '@ParkingSpaceCount')]))
    p.star_dot(lng, lat, size=25, color='red')
    return p
