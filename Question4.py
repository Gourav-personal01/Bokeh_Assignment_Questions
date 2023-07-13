# Q4. What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
# real time?

# Solution -- 

# A Bokeh server is a component of Bokeh that allows you to build interactive web applications that are connected to Python code running on a server. This means that you can create plots that can be updated in real time, as the underlying data changes.

# Below program shows that how can we create interactive plots that can be updated in real time.
import bokeh.plotting as bp
import bokeh.server.server as bs

def my_plot():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    fig = bp.figure()
    fig.line(x, y)
    return fig

server = bs.Server({"/my_plot": my_plot})
server.start()