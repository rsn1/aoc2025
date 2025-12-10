import numpy as np
from scipy.optimize import linprog

with open("input.txt") as f:
    data = [x.split(' ') for x in f.read().splitlines()]

total_ans = 0
for line in data:
    targets = line[-1]
    targets = tuple(map(int,targets[1:-1].split(',')))
    numbers = line[1:-1]
    numbers = [tuple(map(int,x[1:-1].split(','))) for x in numbers]
    n_variables = len(numbers)
    coefficients = np.ones(n_variables)
    rhs = np.array(targets)
    n_equations = len(rhs)
    lhs = np.zeros((n_equations,n_variables))
    for idx, nums in enumerate(numbers):
        for num in nums:
            lhs[num][idx] = 1
    #solve 'lhs @ x = rhs' for x
    res = linprog(coefficients, A_eq = lhs, b_eq = rhs, method='highs', integrality=1)
    sol = np.round(res.x).astype(int)
    total_ans += np.sum(sol)

print(total_ans)
