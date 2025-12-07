import re
import numpy as np

with open("input.txt", "r") as file:
    content = file.read().splitlines()

operations = content[len(content)-1]
operations = re.findall(r'\*|\+|\s+', operations)
width_of_col = max(len(op) for op in operations)

processed = np.array([list(row) for row in content]).transpose()
last_line = np.full((1, width_of_col + 1), ' ') # create a line for parsing convenience
processed = np.append(processed, last_line, axis=0)

total = 0
prob_length = 0
for i, row in enumerate(processed):
    if all(x.isspace() for x in row): # empty row
        nums = []
        for j in range(i - prob_length, i):
            temp_digits = [c for c in processed[j] if (not c.isspace()) and (c not in operations)] # exclude whitespace and operators
            number = int("".join(temp_digits))
            nums.append(number)

        if (processed[i - prob_length][width_of_col] == '+'): # get operation from 1st row, rightmost col of problem
            total += sum(nums)

        elif (processed[i - prob_length][width_of_col] == '*'):
            total += np.prod(nums)

        prob_length = 0
    else:
        prob_length += 1
    
print(total)