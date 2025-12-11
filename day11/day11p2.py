from collections import defaultdict
from functools import cache

with open("input.txt") as f:
    data = [x.split(': ') for x in f.read().splitlines()]

graph = defaultdict(list)

#create graph
for line in data:
    fr = line[0]
    to = line[1].split(' ')
    for node in to:
        graph[fr].append(node)
@cache
def dfs(current_node, found_dac, found_fft):
    if current_node == 'out' and found_dac and found_fft:
        return 1
    if current_node == 'dac':
        found_dac = True
    elif current_node == 'fft':
        found_fft = True
    n_paths = 0
    for n in graph[current_node]:
        n_paths += dfs(n, found_dac, found_fft)
    return n_paths

print(dfs('svr', False, False))
