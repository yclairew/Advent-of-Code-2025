with open("input.txt", "r") as file:
    ingredientRows = file.read().splitlines()

splitIndex = ingredientRows.index("")
ranges = ingredientRows[:splitIndex]

# merge overlapping ranges first
intervals = []
for r in ranges:
    start, end = map(int, r.split('-'))
    intervals.append((start, end))

# sort and merge
intervals.sort()
merged = []
for start, end in intervals:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

# count total IDs
numFreshIDs = sum(end - start + 1 for start, end in merged) # end - start + 1 = numbers in range (inclusive)
print(f"Fresh: {numFreshIDs}")