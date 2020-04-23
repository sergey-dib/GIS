import geopandas as gpd


def getPointCoords(row, geom, coord_type):
    """Calculates coordinates ('x' or 'y') of a Point geometry"""
    if coord_type == 'x':
        return row[geom].x
    elif coord_type == 'y':
        return row[geom].y

points_fp = r"./shp/addresses.shp"

points = gpd.read_file(points_fp)

print(points.head())

# Вычисление координат

points['x'] = points.apply(getPointCoords, geom='geometry', coord_type='x', axis=1)
points['y'] = points.apply(getPointCoords, geom='geometry', coord_type='y', axis=1)

print(points.head())

# Make a copy and drop the geometry column
p_df = points.drop('geometry', axis=1).copy()
print(p_df.head(2))

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, save

# Point DataSource
psource = ColumnDataSource(p_df)
print(psource)

p = figure(title="A map of address points from a Shapefile")

p.circle('x', 'y', source=psource, color='red', size=10)

outfp = r"./bokeh/point_map.html"

save(p, outfp)


from bokeh.models import HoverTool

my_hover = HoverTool()

my_hover.tooltips = [('Address of the point', '@address')]

p.add_tools(my_hover)

outfp = r"./bokeh/point_map_hover.html"
save(p, outfp)


