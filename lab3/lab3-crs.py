import geopandas as gpd
from fiona.crs import from_epsg
import matplotlib.pyplot as plt

# Чтение файла
fp = "addresses.shp"

data = gpd.read_file(fp)

print("Системы координат координат")
print(data.crs)
print(data['geometry'].head())
data_proj = data.copy()
# Перепроектирирование геометрии, заменив значения проекции
data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=3879)

print("Перепроектирированя геометрия,с заменой значения проекции")
print(data_proj['geometry'].head())
print(data_proj.crs)
# Plot the WGS84
data.plot(markersize=6, color="red");

# Add title
plt.title("WGS84 проекция");

plt.show()
plt.tight_layout()

# ETRS GK-25 проекция
data_proj.plot(markersize=6, color="blue");

# Add title
plt.title("ETRS GK-25 проекция");

plt.show()
plt.tight_layout()

# Изменение системы координат
data_proj.crs = from_epsg(3879)
print(data_proj.crs)

# Передача информацию о координатах
data_proj.crs = {'y_0': 0, 'no_defs': True, 'x_0': 25500000, 'k': 1, 'lat_0': 0, 'units': 'm', 'lon_0': 25, 'ellps': 'GRS80', 'proj': 'tmerc'}

print(data_proj.crs)


# Сохранение файлай
outfp = r"addresses_epsg3879.shp"

# Save to disk
data_proj.to_file(outfp)
