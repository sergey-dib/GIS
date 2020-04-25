import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

fp = "./shp-lab/ESRI/London_Borough_Excluding_MHW.shp"
data = "./shp-lab/london-borough-profiles.csv"

map_df = gpd.read_file(fp)

print(map_df.head(5))

map_df.plot()
plt.show()

df = pd.read_csv(data, header=0)

print(df.head(5))

# Выбор полей для работы

df = df[['Area_name', 'Happiness_score_2011-14_(out_of_10)',
         'Anxiety_score_2011-14_(out_of_10)',
         'Population_density_(per_hectare)_2017',
         'Mortality_rate_from_causes_considered_preventable_2012/14']]

# переименование столбцов
data_for_map = df.rename(index=str, columns={
    "Happiness_score_2011-14_(out_of_10)": "happiness",
    "Anxiety_score_2011-14_(out_of_10)": "anxiety",
    "Population_density_(per_hectare)_2017": "pop_density_per_hectare",
    "Mortality_rate_from_causes_considered_preventable_2012/14": "mortality"})

print(data_for_map.head())

# объединение геоданных с очищенным файлом данных csv

merged = map_df.set_index("NAME").join(data_for_map.set_index("Area_name"))

print(merged.head(5))

# установить переменную, которая будет вызывать любой столбец, который мы хотим визуализировать на карте

variable = "pop_density_per_hectare"

# установить диапазон для choropleth

vmin, vmax = 120, 220

# создать фигуру и axes для Matplotlib

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax,
            edgecolor='0.8')

ax.axis("off")

ax.set_title("Предотвратимая смертность в Лондоне",
             fontdict={'fontsize': '25', 'fontweight': '3'})

# создать аннотацию для источника данных
ax.annotate('Source: London Datastore, 2014', xy=(0.1, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=12, color='#555555')

# Создать цветовую  легенды
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# пустой массив для диапазона данных
sm._A = []

cbar = fig.colorbar(sm)

plt.show()

fig.savefig("./plot/map_export.png", dpi=300)




