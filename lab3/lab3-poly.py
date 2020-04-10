from shapely.geometry import Point, Polygon
# Create Point objects
p1 = Point(24.91444, 60.16334)
p2 = Point(24.93025, 60.16846)

# Create a Polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)

p1.within(poly)
p2.within(poly)
print("Проверка значений")
print(p1)
print(p2)
print(poly)
# находится ли p1 внутри многоугольника
print("находится ли точка внутри многоугольника")
p1.within(poly)
p2.within(poly)
print("centroid")
print(p1)
print(poly.centroid)
# Содержит ли полигон точки
print("Содержит ли полигон точки")
print(poly.contains(p1))
print(poly.contains(p2))

from shapely.geometry import LineString, MultiLineString

# Пересечение линий
# Создание линий
line_a = LineString([(0, 0), (1, 1)])
line_b = LineString([(1, 1), (0, 2)])
print("Проверка на пересечение линий")
print(line_a.intersects(line_b))
print(line_a.touches(line_b))

multi_line = MultiLineString([line_a, line_b])
print(multi_line)
# Линия соприкасается с собой
print("Линия соприкасается с собой")
print(line_a.touches(line_a))
print("Линия пересекается с собой?")
print(line_a.intersects(line_a))

