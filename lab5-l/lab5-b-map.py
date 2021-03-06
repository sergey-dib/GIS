import geopandas as gpd


def getPointCoords(row, geom, coord_type):
    """Calculates coordinates ('x' or 'y') of a Point geometry"""
    if coord_type == 'x':
        return row[geom].x
    elif coord_type == 'y':
        return row[geom].y


def getLineCoords(row, geom, coord_type):
    """Returns a list of coordinates ('x' or 'y') of a LineString geometry"""
    if coord_type == 'x':
        return list( row[geom].coords.xy[0] )
    elif coord_type == 'y':
        return list( row[geom].coords.xy[1] )

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


metro_fp = r"./shp/metro.shp"

metro = gpd.read_file(metro_fp)

print(metro.head())

# Вычисление коорднат для линии
metro['x'] = metro.apply(getLineCoords, geom='geometry', coord_type='x', axis=1)
metro['y'] = metro.apply(getLineCoords, geom='geometry', coord_type='y', axis=1)

print(metro.head())

m_df = metro.drop('geometry', axis=1).copy()
msource = ColumnDataSource(m_df)
p = figure(title="A map of the Helsinki metro")
p.multi_line('x', 'y', source=msource, color='red', line_width=3)
outfp = "./bokeh/metro_map.html"
save(p, outfp)

