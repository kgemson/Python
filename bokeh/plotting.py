from bokeh.models.sources import ColumnarDataSource
from motion_detector_bokeh import df

from bokeh.plotting import figure, show
from bokeh.io import output_file
#required for hover...
from bokeh.models import HoverTool,ColumnDataSource

#convert datetimes to string
df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
print(df["Start_string"])

cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime",height=250,width=1000,title="Motion Graph")
p.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

#original version without Hover & CDS uses values from df directly
#q=p.quad(left=df["Start"],right=df["End"],top=1,bottom=0,color="Green")
q=p.quad(left="Start",right="End",top=1,bottom=0,color="Green",source=cds)

output_file("Graph.html")
show(p)