import json

import shapely.geometry
import geopandas_osm.osm

with open('boundary.geojson') as f:
    data = json.load(f)

poly = shapely.geometry.shape(data['features'][0]['geometry'])
df = geopandas_osm.osm.query_osm('way', poly, recurse='down', tags='highway')

roads = df[df.type == 'LineString'][['highway', 'name', 'geometry']]