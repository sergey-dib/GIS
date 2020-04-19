import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from fiona.crs import from_epsg

# Чтение файла
fp = r"addresses.txt"
fp_sh = r"shopping_centers.txt"

data = pd.read_csv(fp_sh, sep=';')
print(data.head())

# Импортировать инструмент геокодирования
from geopandas.tools import geocode

geo = geocode(data['addr'], provider='arcgis')
print(geo.head(2))


# Объединяйте таблицы, используя ключевой столбец «addr»
join = geo.join(data)
print(join.head())

join_buf = join.copy()
join_buf['geometry'] = join_buf.buffer(5)
print("buffer")
print(join_buf.head())

# объединение
join_core = gpd.overlay(join, join_buf, how='intersection')
# Сохранение в файл
outfp = r"./shp/addresses.shp"
join_core.to_file(outfp)

join.plot()
join_buf.plot()
join_core.plot()

import matplotlib.pyplot as plt

plt.tight_layout()
plt.show()


