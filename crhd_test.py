import geopandas as gpd

grid_path = './data/osm_data.shp/gis_osm_landuse_a_free_1.shp'
grids = gpd.read_file(grid_path)
grids = grids.rename(columns = {'Name': 'id'})
grids.to_file('./data/osm_data.shp/gis_osm_landuse_a_free_1.shp')