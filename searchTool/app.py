from flask import Flask, render_template, request, redirect, url_for
from bokeh.embed import components
from bokeh.resources import CDN
from map_plot import my_map
from search_place import find_places
from forms import MapSearchForm
import requests

app = Flask(__name__)


# default page
@app.route('/', methods=['GET', 'POST'])
def homepage():
    p = my_map()
    script1, div1 = components(p)

    search = MapSearchForm(request.form)
    if request.method == 'POST' and search.validate():
        places = find_places(search.search.data)
        return render_template('hello.html', message="TEST",
                               test=True,
                               tables=[places.to_html(classes='data')],
                               titles=places.columns.values,
                               script=script1,
                               div=div1,
                               resources=CDN.render(),
                               form=search)
        # return redirect(url_for('search_results'))

    return render_template('hello.html', message="Welcome to use WheretoPark",
                           script=script1,
                           div=div1,
                           resources=CDN.render(),
                           form=search)


@app.route('/results')
def search_results():
    # print(search.select.data)
    # print(search.search.data)
    # return render_template('hello.html', test="TEST",
    #                        selectData=search.select.data,
    #                        searchData=search.search.data)

    return


if __name__ == '__main__':
    app.run()
