from shapely.geometry import Point, LineString, Polygon

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)
point_type = type(point1)
print(point1)
print(point3D)
print(type(point1))
point_coords = point1.coords
print(type(point_coords))
xy = point_coords.xy
x = point1.x
y = point1.y
print(xy)
print(x)
print(y)
point_dist = point1.distance(point2)
print("Distance between the points is {0:.2f} decimal degrees".format(point_dist))
# LineString
line = LineString([point1, point2, point3])
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(line)
print(line2)
print(type(line))
lxy = line.xy
print(lxy)
line_x = lxy[0]
line_y = line.xy[1]
print(line_x)
print(line_y)

l_length = line.length
l_centroid = line.centroid
centroid_type = type(l_centroid)
print("Length of our line: {0:.2f}".format(l_length))
print("Centroid of our line: ", l_centroid)
print("Type of the centroid:", centroid_type)
# Полігон

poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])
poly_type = poly.geom_type
poly_type2 = type(poly)
print(poly)
print(poly2)
print("Geometry type as text:", poly_type)
print("Geometry how Python shows it:", poly_type2)

world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]
world = Polygon(shell=world_exterior)

world_has_a_hole = Polygon(shell=world_exterior, holes=hole)
print(world)
print(world_has_a_hole)
print(type(world_has_a_hole))
# Атрибути та функції полігона

world_centroid = world.centroid
world_area = world.area
world_bbox = world.bounds
world_ext = world.exterior
world_ext_length = world_ext.length
print("Poly centroid: ", world_centroid)
print("Poly Area: ", world_area)
print("Poly Bounding Box: ", world_bbox)
print("Poly Exterior: ", world_ext)
print("Poly Exterior Length: ", world_ext_length) 

