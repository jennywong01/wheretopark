'''
this is app module for wheretopark tool
'''
import pandas as pd
from flask import Flask, render_template, request
from bokeh.embed import components
from bokeh.resources import CDN
# pylint: disable=E0401
from Utils.map_plot import my_map
# pylint: disable=E0401
from Utils.search_place import find_places
# pylint: disable=E0401
from Utils.forms import MapSearchForm

app = Flask(__name__)

# default page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    """ Define homepage """
    # pylint: disable=invalid-name
    p = my_map(lat=47.6062, lng=-122.3321, zoom=14)
    script1, div1 = components(p)

    search = MapSearchForm(request.form)
    if request.method == 'POST' and search.validate():
        places = find_places(search.search.data)
        path = 'Utils/result.pkl'
        places.to_pickle(path)
        places['name'] = places.index.map(lambda x:
                                          f'<a href=selected_place?result={path}&row={x}>{x} \
                                          {places["name"][x]}</a>')

        return render_template('hello.html', message="Welcome to use WheretoPark",
                               search=True,
                               tables=[places[['name', 'vicinity']].to_html(classes='data',
                                                                            escape=False)],
                               titles=places.columns.values,
                               script=script1,
                               div=div1,
                               resources=CDN.render(),
                               form=search)

    return render_template('hello.html', message="Welcome to use WheretoPark",
                           script=script1,
                           div=div1,
                           resources=CDN.render(),
                           form=search)


@app.route('/selected_place')
def selected_place():
    """Define page after user select the destination"""
    path = request.args.get('result')
    row = int(request.args.get('row'))
    places = pd.read_pickle(path)
    lat = places.iloc[row]['geometry.location.lat']
    lng = places.iloc[row]['geometry.location.lng']
    # pylint: disable=invalid-name
    p = my_map(lat, lng, zoom=16)

    script, div = components(p)

    return render_template('selected.html',
                           script=script, div=div, resources=CDN.render())


if __name__ == '__main__':
    app.run(debug=True)
