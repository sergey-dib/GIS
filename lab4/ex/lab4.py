import geopandas as gpd 
import matplotlib.pyplot as plt


border_fp = "../shp/Helsinki_borders.shp"
grid_fp = "../shp/TravelTimes_to_5975375_RailwayStation.shp"

# чтение файла
grid = gpd.read_file(grid_fp)
hel = gpd.read_file(border_fp)

print(hel.crs)
print(grid.crs)

basemap = hel.plot()
grid.plot(ax=basemap, linewidth=0.02)
plt.show()
plt.tight_layout()


result = gpd.overlay(grid, hel, how='intersection')
result.plot(color="b")
plt.show()
plt.tight_layout()

print(result.head())
print("Длина GeoDataFrame")
print(len(result))
print("Длина grid")
print(len(grid))

resultfp = "../shp_out/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"
result.to_file(resultfp, driver="GeoJSON")

# агрегация данных

result_aggregated = result.dissolve(by="car_r_t")
print(result_aggregated.head())

print(len(result))
print(len(result_aggregated))

