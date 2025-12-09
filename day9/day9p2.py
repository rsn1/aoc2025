from shapely import Polygon, intersection, plotting
from shapely.geometry import box

with open("test.txt") as f:
    data =  [tuple(map(int,x.split(','))) for x in f.read().splitlines()]

#swapped_data = [(y,x) for x,y in data]
polygon = Polygon(data)
print(polygon)
            
exit()
#print(polygon)
#x[0] is col
#x[1] is row
biggest = -1
for x in swapped_data:
    for y in swapped_data[1:]:
        rect = box(min(x[1],y[1]),min(x[0],y[0]), max(x[1], y[1]),  max(x[0],y[0]))
        if not polygon.covers(rect):
            #polygon must fully contain rectangle
            continue
        inter = intersection(polygon,rect)
        if inter.area > biggest:
            biggest = inter.area
            biggestshape = inter

print(biggest)
print(biggestshape)
