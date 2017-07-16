# joy

Geoms to make joy plots using bokeh, written by Sean M. Law

Inspired by Claus Wilke's [ggjoy](https://github.com/clauswilke/ggjoy), the code provided here contains a minimal example for creating a joy plot comparing movie lengths. The key differntiator in this work is the interactive slider that allows the user to define the vertical spacing between each plot.

# Requirements

```
conda install bokeh
conda install pandas
conda install numpy
conda install scipy
```

# Usage

```
bokeh serve --show joy.py
```
