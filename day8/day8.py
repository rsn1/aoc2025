import math 
from collections import defaultdict

with open("input.txt") as f:
    data = [tuple(map(int,x.split(','))) for x in f.read().split('\n')]

def distance(x,y):
    return math.sqrt( (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2  )

P1 = False

#list incase same exact distance multiple times
#key = distance, val = list of points
distances = defaultdict(list)
n_points = len(data)

for idx, x in enumerate(data):
    for y in data[idx+1:]:
        dist = distance(x,y)
        distances[dist].append((x,y))

sortedkeys = sorted(distances.keys())

if P1:
    sortedkeys = sortedkeys[:1000]

#function for P2
def all_same_circuit(dict):
    circuit_to_check = -1
    for _, circuit in dict.items():
        if circuit_to_check == -1:
            circuit_to_check = circuit
        if circuit != circuit_to_check:
            return False
    return True

#map point -> circuit
circuits = defaultdict(int)
current_circuit = 1
for key in sortedkeys:
    boxes = distances[key]
    for box1, box2 in boxes:
        if circuits[box1] != 0 and circuits[box2] != 0 and circuits[box1] == circuits[box2]:
            #both already connected to same circuit
            continue
        elif circuits[box1] != 0 and circuits[box2] != 0 and circuits[box1] != circuits[box2]:
            #both already connected, but to different circuits. merge
            circuit_to_remove = circuits[box1]
            for point, circ in circuits.items():
                if circ == circuit_to_remove:
                    circuits[point] = circuits[box2]
        elif circuits[box1] != 0:
            circuits[box2] = circuits[box1]
        elif circuits[box2] != 0:
            circuits[box1] = circuits[box2]
        else:
            #both 0, assign new circuit
            assert(circuits[box1] == 0)
            assert(circuits[box2] == 0)
            circuits[box1] = current_circuit
            circuits[box2] = current_circuit
            current_circuit += 1
        if not P1 and len(circuits.keys()) == n_points and all_same_circuit(circuits):
            #P2
            print(f"P2: {box1[0]*box2[0]}")
            exit()

#val: circuit, key: list of points
circuitdict = defaultdict(list)
for key,val in circuits.items():
    circuitdict[val].append(key)

circuitsizes = [len(v) for k,v in circuitdict.items()]
circuitsizes.sort(reverse=True)

ans = 1
for x in circuitsizes[:3]:
    ans *= x

print(f"P1: {ans}")