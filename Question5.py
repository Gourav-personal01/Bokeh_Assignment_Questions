# Q5. How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?

# Solution --
# Below is the example for bokeh plot into a web page or dashboard using Flask or Django

import bokeh.plotting as bp
from flask import Flask
import bokeh.embed.components as be

def my_plot():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    fig = bp.figure()
    fig.line(x, y)
    script, div = be.components(fig)
    return script, div

app = Flask(__name__)

@app.route("/")
def index():
    return my_plot()

if __name__ == "__main__":
    app.run(debug=True)