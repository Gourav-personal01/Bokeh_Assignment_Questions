# Q1. How can you create a Bokeh plot using Python code?

# Solution ---
import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()

from bokeh.plotting import figure,output_file,show

from bokeh.sampledata.iris import flowers

output_file('test.html')

p = figure(title = "test Flower")
p.xaxis.axis_label = "paltel lenght"
p.yaxis.axis_label = "paltel width"
p.circle(flowers['petal_length'], flowers['petal_width'])
show(p)
