from collections import defaultdict, deque

with open("input.txt") as f:
    data = [x.split(': ') for x in f.read().splitlines()]

print(data)
graph = defaultdict(list)

#create graph
for line in data:
    fr = line[0]
    to = line[1].split(' ')
    for node in to:
        graph[fr].append(node)

queue = deque(['you'])
n_paths = 0
while len(queue) != 0:
    next = queue.popleft()
    for neighbour in graph[next]:
        queue.append(neighbour)
    if next == 'out':
        n_paths += 1

print(n_paths)


