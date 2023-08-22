import geopandas as gpd
import pandas as pd

save_path = './data/Guangzhou/images/'
grid_path = './data/Guangzhou/grids/天河路网.shp'

gdf = gpd.read_file(grid_path)
# to_keep = ['LINKID', 'LENGTH', 'MAXSPEED', 'MINSPEED']
# gdf = gdf[to_keep]
# df = pd.DataFrame(gdf)
# t_min = []
# for i in range(len(df)):
#     max_speed = df['MAXSPEED'][i]/3.6
#     length = df['LENGTH'][i]
    
#     t_min.append(length/max_speed)

# df['T_min'] = t_min
    
# df.to_csv('./data/Guangzhou/grids/tianhe_grids.csv')    