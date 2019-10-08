import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cf
import cartopy.io.shapereader as shpr

# Retriving the information from web
stt = cf.NaturalEarthFeature(category='cultural', 
    name='admin_0_boundary_lines_land',
    scale='10m',facecolor='none')
stt_prv = cf.NaturalEarthFeature(category='cultural', 
    name='admin_1_states_provinces_lines',
    scale='10m',facecolor='none')
fname = shpr.natural_earth(resolution='10m', category='cultural', name='populated_places')
reader = shpr.Reader(fname)

# Image desing
fig = plt.figure(figsize=(15, 6))

# Main Map
ax = fig.add_subplot(1, 5, (1,4), projection=ccrs.PlateCarree())
ax.set_title('Populated places of the world', fontsize=16)
ax.coastlines()
points = list(reader.geometries())
ax.scatter([point.x for point in points],
           [point.y for point in points],
           transform=ccrs.PlateCarree(),
           s=0.1, c='r')

ax.add_feature(stt, linewidth=0.2, edgecolor='black')



plt.show()