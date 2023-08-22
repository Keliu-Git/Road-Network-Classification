from crhd_generator import PlotCity, PlotCRHD
import geopandas as gpd
from pyproj import CRS, Transformer

# grid_path = './data/Guangzhou/grids/天河路网.shp'
# save_path = './data/Guangzhou/images/'

# grids = gpd.read_file(grid_path)

# grids = grids.rename(columns={'LINKID': 'id'})
# to_keep = ['id', 'geometry', 'LENGTH', 'Attribute']
# grids = grids[to_keep]
# grids.to_file('./data/Guangzhou/grids/grids.shp')

grid_path = './data/Guangzhou/grids/grids.shp'


grids = gpd.read_file(grid_path)
# target_crs = CRS.from_epsg(32610)
# grids_reprojected = grids.to_crs(target_crs)
# grids['length_meters'] = grids_reprojected['geometry'].length

# print(grids)
# grids.to_file('./data/Guangzhou/grids/grids.shp')