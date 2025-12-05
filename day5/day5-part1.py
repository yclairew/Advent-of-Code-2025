with open("input.txt", "r") as file:
    ingredientRows = file.read().splitlines()

splitIndex = ingredientRows.index("")
ranges = ingredientRows[:splitIndex]
ingredients = ingredientRows[splitIndex + 1:]

ingredientVals = list(map(int, ingredients))

freshCount = 0

for i, val in enumerate(ingredientVals):
    isFresh = False

    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        if (start <= val <= end):
            isFresh = True
            break
    
    if isFresh:
        freshCount += 1

print(f"Fresh: {freshCount}")