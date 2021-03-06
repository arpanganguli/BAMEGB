# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# add PYTHONPATH
# import sys
# sys.path.insert(0, '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages')

# import packages
import bokeh
import sqlalchemy
import geopandas as gpd
import matplotlib.pyplot as plt

# file path
shp_path = r'/Users/arpanganguli/Documents/Professional/Projects/BAMEGB/Shapefiles/infuse_dist_lyr_2011-2/infuse_dist_lyr_2011.shp'
shp_GB = gpd.read_file(shp_path)

fig = plt.figure()
shp_GB.plot(figsize=(10,10), edgecolor="purple", facecolor="None")
plt.axis('off')