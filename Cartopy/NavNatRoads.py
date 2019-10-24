#import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
#import cartopy
#import cartopy.feature as cfeature
#import numpy as np
import geopandas as gpd
from os.path import expanduser
import fiona
import geopandas_osm

mydir = expanduser("~/GitHub/IBM-Dojo")
gdb_file = mydir + '/Cartopy/NavNatData/Navajo_Roads/data/v93/temp9_data0_data0.gdb/'

# Get all the layers from the .gdb file 
layers = fiona.listlayers(gdb_file)

print layers

for layer in layers:
    gdf = gpd.GeoDataFrame.from_file(gdb_file)
    print 'good'
    # Do stuff with the gdf