import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

import matplotlib.pyplot as plt

# Популяция
fp = "Vaestotietoruudukko_2015.shp"
pop = gpd.read_file(fp)
print(pop.head())
pop = pop.rename(columns={'ASUKKAITA': 'pop15'})
print(pop.columns)
selected_cols = ['pop15', 'geometry']
pop = pop[selected_cols]
print(pop.tail(2))

# pop_proj = pop.copy()
# pop_proj['geometry'] = pop_proj['geometry'].to_crs(epsg=3879)
addr_fp = r"./shp/addresses_epsg3879.shp"
addresses = gpd.read_file(addr_fp)

print(addresses.head(2))
print("Сравнение")
print(addresses.crs)
print(pop.crs)
print(addresses.crs == pop.crs)
join = gpd.sjoin(addresses, pop, how="inner", op="within")
print(join.head())

outfp = r"./shp/addresses_pop15_epsg3979.shp"

# Save to disk
join.to_file(outfp)

# join.plot(column='pop15', cmap="Reds", markersize=7, scheme='natural_breaks', legend=True)
join.plot(column='pop15', cmap="Reds", markersize=7, scheme='natural_breaks', legend=True)
plt.title("Количество жителей, живущих рядом с точкой")
plt.show()
