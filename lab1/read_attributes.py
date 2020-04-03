from shapely.geometry import Point, LineString, Polygon


def getCentroid(geom):
    return (geom.centroid)


def getArea(geom):
    return (geom.area)


def getLength(geom):
    if type(geom) == LineString:
        return (geom.length)
    elif type(geom) == Polygon:
        return (geom.exterior.length)
    else:
        return 'Неверная геометрия.'


poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
line = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

print(getCentroid(poly))
print(getCentroid(line))
print(getArea(poly))
print(getArea(line))
print(getLength(poly))
print(getLength(line))

point1 = Point(5.0, 4.2)
print(getCentroid(point1))
print(getArea(point1))
print(getLength(point1))
