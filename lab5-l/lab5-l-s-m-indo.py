import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

fp = "./shp-lab/IDN_adm/IDN_adm1.shp"
data = "./shp-lab/data_province.csv"
map_df = gpd.read_file(fp)
# check the GeoDataframe
print(map_df.head(5))

map_df.plot()
plt.rcParams['figure.figsize'] = [50, 70]
plt.show()

province = pd.read_csv(data, sep=";")
print(province.head(5))

# добавление к геоданным данных csv

merged = map_df.merge(province, how='left', left_on="NAME_1",
                      right_on="province")
merged = merged[['province', 'geometry', 'population_2015', 'area_km2',
                 'population_density_per_km2', \
                 'cities_regencies', 'cities', 'regencies']]
print(merged.head(5))

# установить столбец значений, который будет отображаться
variable = 'cities_regencies'
vmin, vmax = 0, 50
fig, ax = plt.subplots(1, figsize=(30, 10))
ax.axis('off')
ax.set_title('# городов в каждом регионе',
             fontdict={'fontsize': '25', 'fontweight': '3'})
ax.annotate(
    'Source: Wikipedia - https://en.wikipedia.org/wiki/Provinces_of_Indonesia',
    xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')

# легенда
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# пустой массив для диапазона данных
sm.set_array([])

merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
merged['coords'] = [coords[0] for coords in merged['coords']]
for idx, row in merged.iterrows():
    plt.annotate(s=row['province'], xy=row['coords'],horizontalalignment='center')

fig.colorbar(sm, orientation="horizontal", fraction=0.036, pad=0.1, aspect = 30)

merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')


plt.show()

fig.savefig('./plot/map.png', dpi=300)
