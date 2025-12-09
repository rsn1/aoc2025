from shapely import Polygon
from shapely.geometry import box
import matplotlib.pyplot as plt

with open("input.txt") as f:
    data =  [tuple(map(int,x.split(','))) for x in f.read().splitlines()]

polygon = Polygon(data)
biggest = -1
for x in data:
    for y in data[1:]:
        rect = box(min(x[0],y[0]), min(x[1],y[1]), max(x[0],y[0]), max(x[1], y[1]))
        if not polygon.covers(rect):
            #polygon must fully contain rectangle
            continue
        area = (abs(x[0]-y[0])+1) * (abs(x[1]-y[1])+1)
        if area > biggest:
            biggest = area
            biggestshape = rect

print(biggest)
#x1, y1 = polygon.exterior.xy
#x2, y2 = biggestshape.exterior.xy
#plt.plot(x1,y1)
#plt.plot(x2,y2)
#plt.show()
