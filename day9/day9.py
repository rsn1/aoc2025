with open("input.txt") as f:
    data =  [tuple(map(int,x.split(','))) for x in f.read().splitlines()]

areas = []
for x in data:
    for y in data[1:]:
        dist_x, dist_y = abs(x[0]-y[0])+1, abs(x[1]-y[1])+1
        area = dist_x * dist_y
        areas.append(area)

areas.sort(reverse=True)
print(areas[0])