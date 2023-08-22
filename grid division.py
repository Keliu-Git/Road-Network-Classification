import geopandas as gpd
import numpy as np
from shapely.geometry import Point, Polygon, box

# Load the original shapefile
grid_path = './data/Guangzhou/grids/广州1000m网格_wgs84.shp'
og = gpd.read_file(grid_path)
og.crs = 'EPSG:4326'

geometry_lst = []

# Create a new grid of points at 500m intervals
new_grid_points = []
for index, row in og.iterrows():
    print(index)
    original_polygon = row.geometry
    (minx, miny, maxx, maxy) = original_polygon.bounds
    
    # check if square
    if (original_polygon.area / original_polygon.minimum_rotated_rectangle.area) > .99:
    
        center = original_polygon.centroid
        
        box1 = (minx, miny, center.x, center.y)
        box2 = (minx, center.y, center.x, maxy)
        box3 = (center.x, miny, maxx, center.y)
        box4 = (center.x, center.y, maxx, maxy)
        
        box1 = box(*box1)
        box2 = box(*box2)
        box3 = box(*box3)
        box4 = box(*box4)
        
        geometry_lst.extend([box1, box2, box3, box4])
    
new_geometry = gpd.GeoSeries(geometry_lst)
new_shape = gpd.GeoDataFrame(new_geometry, columns=['geometry'], crs='EPSG:4326')

intersect = gpd.overlay(new_shape, og)
intersect['id'] = intersect.index
intersect['osm_id'] = intersect.index
intersect.to_file('./data/Guangzhou/grids/gz_500.shp')
