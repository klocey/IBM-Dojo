import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
import numpy as np

central_lat = (-111.9 + -108.2)/2
central_lon = (34.4 + 36.9)/2
extent = [-111.9, -108.2, 34.4, 36.9]
central_lon = np.mean(extent[:2])
central_lat = np.mean(extent[2:])

rivers_10m = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '10m')
bound_10m = cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces', '10m')
roads_10m = cfeature.NaturalEarthFeature('cultural', 'roads', '10m')
cities_10m = cfeature.NaturalEarthFeature('cultural', 'populated_places', '10m')



plt.figure(figsize=(12, 6))

ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
ax.set_extent(extent)

ax.add_feature(cartopy.feature.LAND, edgecolor='black')
ax.add_feature(rivers_10m, facecolor='None', edgecolor='b')
ax.add_feature(bound_10m, facecolor='None', edgecolor='k')
ax.add_feature(roads_10m, facecolor='None', edgecolor='0.7')
ax.add_feature(cities_10m, color='k')
#ax.gridlines()


lat1, lon1 = 36.3061, -109.2208

plt.plot([lon1], [lat1], color='r', 
         linewidth=2, marker='o',
         transform=ccrs.Geodetic())

