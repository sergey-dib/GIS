import geopandas as gpd
import matplotlib.pyplot as plt


grid_fp = r"./shp/TravelTimes_to_5975375_RailwayStation.shp"
roads_fp = r"./shp/roads.shp"
metro_fp = r"./shp/metro.shp"

grid = gpd.read_file(grid_fp)
roads = gpd.read_file(roads_fp)
metro = gpd.read_file(metro_fp)


gridCRS = grid.crs

# изменение геометрии
roads['geometry'] = roads['geometry'].to_crs(crs=gridCRS)
metro['geometry'] = metro['geometry'].to_crs(crs=gridCRS)


my_map = grid.plot(column="car_r_t", linewidth=0.03, cmap="Reds", scheme="quantiles", k=9,
alpha=0.9)
roads.plot(ax=my_map, color="grey", linewidth=1.5)
metro.plot(ax=my_map, color="red", linewidth=2.5)
plt.tight_layout()
plt.show()
outfp = r"./plot/static_map.png"
plt.savefig(outfp, dpi=300)


