import geopandas as gpd
import matplotlib.pyplot as plt

fp = "./shp/addresses_epsg3879.shp"

data = gpd.read_file(fp)

data_proj = data.copy()

data_proj['geometry'] = data_proj.geometry.buffer(5 * 1000)

print(data_proj.head(5))

data_proj.plot()
plt.show()
