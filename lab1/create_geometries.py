from shapely.geometry import Point, LineString, Polygon


def createPointGeom(x_coord, y_coord):
    point1 = Point(x_coord, y_coord)
    return print("Print point: ", point1)


def createLineGeom(points):
    if all(isinstance(x, Point) for x in points) is True:
        return print("Print line: ", LineString(points))


def createPolyGeom(body):
    if type(body) == list:
        return print("Print polygon: ", (Polygon(body)))
    else:
        print('Ошибка')


resPoint = createPointGeom(2.2, 4.2)

PostPoint = [Point(2.2, 4.2), Point(7.2, -25.1), Point(9.26, -2.456)]
resLine = createLineGeom(PostPoint)

polygon = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]
resPolygon = createPolyGeom(polygon)
