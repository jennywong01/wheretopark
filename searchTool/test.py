# Importing required functions

from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure

# Flask constructor
app = Flask(__name__)


# Root endpoint
@app.route('/')
def homepage():
    title = 'home'

    # First Plot
    p = figure(plot_width=400, plot_height=400)
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

    # Second Plot
    p2 = figure(plot_width=400, plot_height=400)
    p2.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5)

    script, div = components(p)
    script2, div2 = components(p)

    return render_template('charts.html', title=title, script=script,
                           div=div, script2=script2, div2=div2)


# Main Driver Function
if __name__ == '__main__':
    # Run the application on the local development server
    app.run()
