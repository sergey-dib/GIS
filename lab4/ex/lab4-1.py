import geopandas as gpd
import numpy as np

border_fp = "../shp/Helsinki_borders.shp"
grid_fp = "../shp/TravelTimes_to_5975375_RailwayStation.shp"

grid = gpd.read_file(grid_fp)
hel = gpd.read_file(border_fp)
b = 10
row_cnt = len(grid)
iterations = int(np.ceil(row_cnt / b))
final = gpd.GeoDataFrame()

# Установите начальный и конечный индексы в соответствии с размером пакета
start_idx = 0
end_idx = start_idx + b

for iteration in range(iterations):
    print("Iteration: %s/%s" % (iteration, iterations))

    # Make an overlay analysis using a subset of the rows
    result = gpd.overlay(grid[start_idx:end_idx], hel, how='intersection')

    # Append the overlay result to final GeoDataFrame
    final = final.append(result)

    # Update indices
    start_idx += b
    end_idx = start_idx + b

outfp = "../shp_out/overlay_analysis_speedtest.geojson"
final.to_file(outfp, driver="GeoJSON")
