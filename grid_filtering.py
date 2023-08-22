import geopandas as gpd

gz_grid = gpd.read_file('./data/Guangzhou/grids/gz_500.shp')
bound = gpd.read_file('./data/Guangzhou/boundary/天河区_wgs84.shp')

tianhe_grid = bound.overlay(gz_grid, how='intersection')

to_keep = ['COUNTY', 'CITY', 'x', 'y', 'OBJECTID',
      'Shape_Leng', 'Shape_Area', 'id_1', 'osm_id', 'geometry']

tianhe_grid = tianhe_grid[to_keep]
tianhe_grid = tianhe_grid.rename(columns = {'id_1': 'id'})

tianhe_grid.to_file('./data/Guangzhou/grids/tianhe_500.shp')
