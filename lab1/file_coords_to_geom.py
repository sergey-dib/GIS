import pandas as pd
from shapely.geometry import Point, LineString
dF = pd.read_csv('travelTimes_2015_Helsinki.txt', sep=';', usecols=['from_x', 'from_y', 'to_x', 'to_y'])
print(dF)
origPoints = []
destPoints = []
for index, row in dF.iterrows():
    origPoints.append(Point(row['from_x'], row['from_y']))
    destPoints.append(Point(row['to_x'], row['to_y']))

print(LineString(origPoints))
print(LineString(destPoints))