with open("input.txt", "r") as file:
    content = file.read().splitlines()

problems = content[0:(len(content)-1)] # len(content) = num "rows"
temp_o = content[len(content)-1]
operations = [o for o in temp_o if o.strip()]

import numpy as np
processed = []
for problem in problems:
    temp = problem.split(" ")
    numbers = [n for n in temp if n.strip()]
    processed.append(numbers)

processed_np_arr = np.array(processed)
transposed_arr = processed_np_arr.T

total = 0
num_rows, num_cols = np.shape(transposed_arr)
for i in range(0, num_rows):
    int_arr = transposed_arr.astype(int)
    if operations[i] == '+':
        total += sum(int_arr[i])
    elif operations[i] == '*':
        total += np.prod(int_arr[i])

print(total)