from crhd_generator import PlotCity, PlotCRHD
import geopandas as gpd

save_path = './data/Guangzhou/images/'
grid_path = './data/Guangzhou/grids/tianhe_gridded.shp'

grids = gpd.read_file(grid_path)

grids.crs = 'EPSG:4326'

coords = {
    'x': [],
    'y': []
    }

img = PlotCRHD(center_point=(23.222421, 113.346080), 
               dist=1000, 
               name='Guanghzou',
               save_path='./data/'
              )    