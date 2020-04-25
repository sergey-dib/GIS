import geopandas as gpd
import pandas as pd
import json
from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer

from bokeh.io import curdoc, output_notebook
from bokeh.models import Slider, HoverTool
from bokeh.layouts import widgetbox, row, column


# Определите функцию, которая возвращает json_data для года, выбранного пользователем
def json_data(selectedYear):
    yr = selectedYear
    df_yr = df[df['year'] == yr]
    merged = gdf.merge(df_yr, left_on='country_code', right_on='code',
                       how='left')
    merged.fillna('No data', inplace=True)
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return json_data


# Определите функцию обратного вызова: update_plot
def update_plot(attr, old, new):
    yr = slider.value
    new_data = json_data(yr)
    geosource.geojson = new_data
    p.title.text = 'Share of adults who are obese, %d' % yr


shapefile = './shp-lab/data/countries_110m/ne_110m_admin_0_countries.shp'
datafile = './shp-lab/data/obesity.csv'

gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

# переименовать колонки.
gdf.columns = ['country', 'country_code', 'geometry']
print(gdf.head(5))

print(gdf[gdf['country'] == 'Antarctica'])
# Отбросить строку, соответствующую «Антарктиде»
gdf = gdf.drop(gdf.index[159])

df = pd.read_csv(datafile, names=['entity', 'code', 'year', 'per_cent_obesity'],
                 skiprows=1)
print(df.head(5))

print(df.info())
# df[df['code']].isnull()
# Фильтровать данные за 2016 год.
df_2016 = df[df['year'] == 2016]

# Слияние фреймов данных gdf и df_2016
merged = gdf.merge(df_2016, left_on='country_code', right_on='code', how='left')

# Замените значения NaN на строку «Нет данных».
merged.fillna('No data', inplace=True)
# Чтение данных в json
merged_json = json.loads(merged.to_json())
# Преобразовать в объект типа String
# json_data = json.dumps(merged_json)

# Входной источник GeoJSON, содержащий функции для построения графиков

geosource = GeoJSONDataSource(geojson=json_data(2016))

# Построение карты
# Определите последовательную многоцветную цветовую палитру
palette = brewer['YlGnBu'][8]
# Обратный порядок цвета, так что темно-синий является самым высоким ожирением
palette = palette[::-1]
# Создайте экземпляр LinearColorMapper, который линейно отображает числа в диапазоне в последовательность цветов
color_mapper = LinearColorMapper(palette=palette, low=0, high=40,
                                 nan_color='#d9d9d9')
# Определите пользовательские метки для цветной панели.
tick_labels = {'0': '0%', '5': '5%', '10': '10%', '15': '15%', '20': '20%',
               '25': '25%', '30': '30%', '35': '35%', '40': '>40%'}

# Добавить инструмент наведения
hover = HoverTool(tooltips=[('Страна/регион', '@country'),
                            ('% ожирение', '@per_cent_obesity')])

# Создать цветную полосу

color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500,
                     height=20,
                     border_line_color=None, location=(0, 0),
                     orientation='horizontal',
                     major_label_overrides=tick_labels)

# Создать фигуру объекта
p = figure(title='Доля взрослых, страдающих ожирением, 2016', plot_height=600,
           plot_width=950, toolbar_location=None, tools=[hover])
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# Добавить патч рендерер на рисунок
p.patches('xs', 'ys', source=geosource,
          fill_color={'field': 'per_cent_obesity', 'transform': color_mapper},
          line_color='black', line_width=0.25, fill_alpha=1)

p.add_layout(color_bar, 'below')

slider = Slider(title='Year', start=1975, end=2016, step=1, value=2016)
slider.on_change('value', update_plot)
# Создайте макет столбца для виджета (слайдера) и графика и добавьте его в текущий документ
layout = column(p, widgetbox(slider))
curdoc().add_root(layout)

# show(p)
show(layout)
