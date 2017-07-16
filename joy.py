import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider, Range1d
from bokeh.layouts import layout
from bokeh.io import curdoc
from scipy.stats import gaussian_kde

raw_df = pd.read_csv('movies.csv', index_col=0)
raw_df = raw_df[raw_df['year'] >= 1920]
raw_df.head()

x = np.linspace(-100, 200, 51)
groups = raw_df.groupby('year')
df = pd.DataFrame(index=x)
for year, group in groups:
    dat = group['length']
    pdf = gaussian_kde(dat.values)
    df[str(year)] = pdf(x)

def get_movie_data(df, spacing=0.0):
    n = len(df.columns)
    data = dict(
                xs=np.vsplit(np.array([df.index.values,]*n), n),  # Repeat index n times
                ys=np.vsplit(df.T.values + (np.array(range(n)) * spacing).reshape(n,1), n)
            )
    return data

cds = ColumnDataSource(get_movie_data(df))

p = figure()
p.patches(xs='xs', ys='ys', source=cds, fill_color='grey')
p.multi_line(xs='xs', ys='ys', source=cds, color='black')
p.x_range = Range1d(0, 200)

def slider_update(attrname, old, new):
    spacing = s.value
    cds.data = get_movie_data(df, spacing)
    
s = Slider(start=0.0, end=0.01, value=0.0, step=.0001)
s.on_change('value', slider_update)

l = layout([[p], [s]], sizing_mode='stretch_both')

curdoc().add_root(l)
