# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:10:18 2022

@author: Nikita Goel
"""

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, LabelSet
import pandas as pd

output_file('case_study_2.html')
def line_plot(customer_id, revenue_2015, revenue_2016, revenue_2017):
    line_chart_obj = figure(width=500, height=500, title="Revenue comparison of existing customers for year 2015-2017")

    line_chart_obj.line(customer_id, revenue_2015, line_width=2, color='red', legend_label="2015")
    line_chart_obj.line(customer_id, revenue_2016, line_width=2, color='blue', legend_label="2016")
    line_chart_obj.line(customer_id, revenue_2017, line_width=2, color='green', legend_label="2017")
    line_chart_obj.xaxis.ticker = list(range(0,11))
    line_chart_obj.min_border = 0 
    line_chart_obj.outline_line_color = None 
    line_chart_obj.xaxis.axis_line_color = None
    line_chart_obj.xaxis.minor_tick_line_color = None  
    line_chart_obj.xgrid.grid_line_color = None
    line_chart_obj.yaxis.axis_line_color = None
    line_chart_obj.yaxis.major_label_text_color = "white"
    line_chart_obj.ygrid.grid_line_color = None
    line_chart_obj.yaxis.major_tick_line_color = None  
    line_chart_obj.yaxis.minor_tick_line_color = None

    return line_chart_obj


def bar_plot(customer_id, total_customers):
    bar_chart_obj = figure(width=500, height=500, title="Total customers across year 2015-2017")
    bar_chart_obj.vbar(x=customer_id, top=total_customers, width=0.3, color="grey", fill_color=None)
    source = ColumnDataSource(data=dict(x=customer_id, y=total_customers, y_label=[str(i) for i in total_customers]))
    labels= LabelSet(x='x', y='y', text='y_label', source=source, text_align='center', render_mode='canvas')
    bar_chart_obj.add_layout(labels)
    bar_chart_obj.xaxis.ticker = list(range(0,11))
    bar_chart_obj.min_border = 0 
    bar_chart_obj.outline_line_color = None 
    bar_chart_obj.xaxis.axis_line_color = None
    bar_chart_obj.xaxis.minor_tick_line_color = None  
    bar_chart_obj.xgrid.grid_line_color = None
    bar_chart_obj.yaxis.axis_line_color = None
    bar_chart_obj.yaxis.major_label_text_color = "white"
    bar_chart_obj.ygrid.grid_line_color = None
    bar_chart_obj.yaxis.major_tick_line_color = None  
    bar_chart_obj.yaxis.minor_tick_line_color = None
    return bar_chart_obj

    
df = pd.read_csv('visual_observation.csv')
customer_id = df['customer_id'].tolist()[:10]
revenue_2015 = df['revenue_2015'].tolist()[:10]
revenue_2016 = df['revenue_2016'].tolist()[:10]
revenue_2017 = df['revenue_2017'].tolist()[:10]
year = df['year'].tolist()
total_customers = df['total customers'].tolist()
line_chart_plot = line_plot(customer_id, revenue_2015, revenue_2016, revenue_2017)
bar_chart_plot = bar_plot(customer_id, total_customers)

dashboard = gridplot([[line_chart_plot, bar_chart_plot]], width=500, height=500, toolbar_location=None)

show(dashboard)