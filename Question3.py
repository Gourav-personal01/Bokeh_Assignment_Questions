# Q3. How can you customize the appearance of a Bokeh plot, including the axes, title, and legend?

# Solution -- 
# We can use the below program to plot the axes, title and legend
import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()

from bokeh.plotting import figure,output_file,show

from bokeh.sampledata.iris import flowers

output_file('test.html')

x = [2,3,4,5,6]
y = [3,4,5,6,7]
output_file("line.html")
p= figure(title = "draw a line graph")
p.scatter(x,y,fill_color = 'red',legend_label = "red_points",size = 20)
show(p)