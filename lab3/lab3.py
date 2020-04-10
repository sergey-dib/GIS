import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from fiona.crs import from_epsg

# Чтение файла
fp = r"addresses.txt"

data = pd.read_csv(fp, sep=';')
print(data.head())

# Импортировать инструмент геокодирования
from geopandas.tools import geocode

geo = geocode(data['addr'], provider='arcgis')
print(geo.head(2))


# Объединяйте таблицы, используя ключевой столбец «addr»
join = geo.join(data)
print(join.head())

# Сохранение в файл
outfp = r"addresses.shp"
join.to_file(outfp)

join.plot()

import matplotlib.pyplot as plt

plt.tight_layout()
plt.show()


