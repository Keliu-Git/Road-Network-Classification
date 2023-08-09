from morphoindex_generator import get_MorphoIndex, prob_calculator
import geopandas as gpd

grid_path = './data/Singapore/grids/grids.shp'
grids = gpd.read_file(grid_path)

road_path = './data/Singapore/osm_data.shp/gis_osm_roads_free_1.shp'
building_path = './data/Singapore/osm_data.shp/gis_osm_buildings_a_free_1.shp'
landuse_path = './data/Singapore/osm_data.shp/gis_osm_landuse_a_free_1.shp'
save_path =  './data/Singapore/grids/grids_morpho.shp'

# get_MorphoIndex function test
# grids = get_MorphoIndex(grid_path, road_path, building_path, landuse_path, save_path, 
#                         get_intersection=False,  # whether to calculate intersection density
#                         drop_nonbuilt=True  # whether to drop grids without buildings and roads.
#                       )

# print(grids)

# prob_calculator function test
# Specify the filepaths.
model_path = './model/ResNet34-4class6/ResNet34-4class6.h5'  # filepath of your model
grid_path = './data/Singapore/grids/grids.shp'
image_path = './data/Singapore/images/'   # filepath of your CRHD images
save_path = './data/Singapore/grids/grids_probs.shp'

pc = prob_calculator(channeles=3)  # Define a prob_calculator that deal with images of three channeles
pc.load_model(model_path)  # Load the road network classification model
grids = pc.getProb(grid_path, image_path, save_path)

