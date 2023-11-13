#Setup- before you start create a new 'mapping' environment following the instructions from class and make sure you have the following packages installed
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd

# %%
# 1. Open the arizona_huc8_shapefil and the arizona_shapefile following the example we did in class. 
file =  os.path.join('../data/arizona_huc8_shapefile', 'WBDHU8.shp')
arizona = gpd.read_file(file)
# 2. Explore their properties and attributes and be able to explain (1) what type of geometry each is, (2) how many features there are, (3) what attributes each feature has. 
type(arizona)
arizona.head()
arizona.columns
arizona.shape
arizona.geom_type
arizona.crs
arizona.total_bounds
# 3. Plot each dataset. You can plot them separately but also try plotting subsets and plotting them on top of each other. 
# %%
fig, ax = plt.subplots(figsize=(10, 10))
arizona.plot(ax=ax)
plt.show()
fig, ax = plt.subplots(figsize=(10, 10))
arizona.plot(column='areasqkm', categorical=False, 
                legend=True, markersize=45, cmap='OrRd',
                ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
plt.show()
# %%
fig, ax = plt.subplots(figsize=(10, 10))
arizona.plot(column='areaacres', categorical=False, 
                legend=True, markersize=45, cmap='PiYG',
                ax=ax)
ax.set_title("Arizona acres area\n (sq km)")
plt.show()
# %%
