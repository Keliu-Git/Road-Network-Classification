from morphoindex_generator import get_MorphoIndex, get_index, prob_calculator
import geopandas as gpd

# get_MorphoIndex function test

# road_path = './data/Guangzhou/osm_data.shp/roads.shp'
# building_path = './data/Guangzhou/osm_data.shp/building.shp'
# landuse_path = './data/Guangzhou/osm_data.shp/land.shp'
# grid_path = './data/Guangzhou/grids/tianhe_500.shp'
# save_path =  './data/Guangzhou/grids/grids_morpho.shp'

# grids = get_MorphoIndex(grid_path, road_path, building_path, landuse_path,
#                           save_path, 
#                         get_intersection=False,  # whether to calculate intersection density
#                         drop_nonbuilt=False  # whether to drop grids without buildings and roads.
#                       )

# Specify the filepaths.
model_path = './model/ResNet34-4class6/ResNet34-4class6.h5'  # filepath of your model
grid_path = './data/Guangzhou/grids/th_500.shp'
image_path = './data/Guangzhou/images/'   # filepath of your CRHD images
save_path = './data/Guangzhou/grids/grids_probs.shp'

pc = prob_calculator(channeles=3)  # Define a prob_calculator that deal with images of three channeles
pc.load_model(model_path)  # Load the road network classification model
grids = pc.getProb(grid_path, image_path, save_path)