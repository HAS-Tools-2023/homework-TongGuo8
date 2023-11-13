#%%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx
# %%
# The data from class
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
file = os.path.join('data/WBD_15_HU2_GDB', 'WBD_15_HU2_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")
HUC8 =gpd.read_file(file, layer="WBDHU8")
#%%
# Data from class
file =  os.path.join('data/arizona_huc8_shapefile', 'WBDHU8.shp')
arizona = gpd.read_file(file)
#%%
# Main rivers and streams in US
# Data from https://hub.arcgis.com/datasets/esri::usa-rivers-and-streams/explore
file=os.path.join('data/USA_Rivers_and_Streams-shp')
stream= gpd.read_file(file)
stream.State.unique()
stream_AZ=stream[stream['State']=='AZ']
stream.crs
#%%
# Data from class:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
file =  os.path.join('data/gagesii_shapefile', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)
#%%
# Data from class
# https://www.sciencebase.gov/catalog/item/59fa9f59e4b0531197affb13 
file =  os.path.join('data/arizona_shapefile', 'tl_2016_04_cousub.shp')
state = gpd.read_file(file)
state_boundary = state[['LSAD', 'geometry']]
cont_az = state_boundary.dissolve(by='LSAD')
# Plot the dissolved data
fig, ax = plt.subplots(figsize=(10, 6))
cont_az.reset_index().plot(column='LSAD',
                            ax=ax)
ax.set_axis_off()
plt.axis('equal')
plt.show() 
# %%
fig, ax = plt.subplots(figsize=(10, 10))
HUC6.boundary.plot(ax=ax, color=None,
                edgecolor='black', linewidth=1)
ax.set_title("HUC Boundaries")
plt.show()
# %%
# The forecast river xy
point_list = np.array([[-111.7891667, 34.44833333]])
point_geom = [Point(xy) for xy in point_list]
point_geom
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)
# Choose Arizona
gages.STATE.unique()
gages_AZ=gages[gages['STATE']=='AZ']
gages_AZ.shape
#%%
# Project different coordinate system
points_project = point_df.to_crs(gages_AZ.crs)
HUC6_project = HUC6.to_crs(gages_AZ.crs)
stream_AZ_project=stream_AZ.to_crs(gages_AZ.crs)
state_project=cont_az.to_crs(gages_AZ.crs)
# Plot the map
fig, ax = plt.subplots(figsize=(10, 10))
HUC6_project.plot(ax=ax, edgecolor='black',color='orange', alpha=0.6,
                            label='huc6',linewidth=1.5)
state_project.boundary.plot(ax=ax, edgecolor='maroon',color=None, 
                            linewidth=1.5, label='Arizona boundary')

gages_AZ.plot(column='DRAIN_SQKM',marker='^', markersize=40, color='green',
              edgecolor='black',label='Gages',
              ax=ax)
points_project.plot(ax=ax, color='violet', marker='*',edgecolor='crimson',
                    markersize=150,label='Forecast stream')
stream_AZ_project.plot(ax=ax,color='darkcyan',linewidth=0.8,label='Rivers')
ctx.add_basemap(ax, source=ctx.providers.OpenTopoMap.url)
ax.legend(prop={'size':10})
# %%
# The way can change basemap 
ctx.providers.keys()
ctx.providers.OpenTopoMap.keys()
# %%

# %%
