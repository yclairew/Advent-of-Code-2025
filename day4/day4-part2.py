with open("input.txt", "r") as file:
    content = file.read()
    rows = content.split("\n")

removed = 0
indexes = []

while True:
    rollsAccessible = 0
    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])): 
            if (rows[i][j] == '@'):
                adjacentRolls = 0
                if i == 0: # only check left, right, and below
                    if j == 0:
                        rollsAccessible += 1
                        rows[i] = list(rows[i])
                        rows[i][j] = 'x'
                        rows[i] = "".join(rows[i])
                        removed += 1
                        tempList = [i, j]
                        indexes.append(tempList)
                    elif j == (len(rows[i]) - 1):
                        rollsAccessible += 1
                        rows[i] = list(rows[i])
                        rows[i][j] = 'x'
                        rows[i] = "".join(rows[i])
                        removed += 1
                        tempList = [i, j]
                        indexes.append(tempList)
                    else:
                        if rows[i][j-1] == '@': # left
                            adjacentRolls += 1
                        if rows[i][j+1] == '@': # right
                            adjacentRolls += 1
                        if rows[i+1][j-1] == '@': # below left
                            adjacentRolls += 1
                        if rows[i+1][j] == '@': # below middle
                            adjacentRolls += 1
                        if rows[i+1][j+1] == '@': # below right
                            adjacentRolls += 1

                        if adjacentRolls < 4:
                            rollsAccessible += 1
                            rows[i] = list(rows[i])
                            rows[i][j] = 'x'
                            rows[i] = "".join(rows[i])
                            removed += 1 
                            tempList = [i, j]
                            indexes.append(tempList)   

                elif i == (len(rows) - 1): # only check left, right, and above
                    if j == 0:
                        rollsAccessible += 1
                        rows[i] = list(rows[i])
                        rows[i][j] = 'x'
                        rows[i] = "".join(rows[i])
                        removed += 1
                        tempList = [i, j]
                        indexes.append(tempList)
                    elif j == (len(rows[i]) - 1):
                        rollsAccessible += 1
                        rows[i] = list(rows[i])
                        rows[i][j] = 'x'
                        rows[i] = "".join(rows[i])
                        removed += 1
                        tempList = [i, j]
                        indexes.append(tempList)
                    else:
                        if rows[i][j-1] == '@': # left
                            adjacentRolls += 1
                        if rows[i][j+1] == '@': # right
                            adjacentRolls += 1
                        if rows[i-1][j-1] == '@': # above left
                            adjacentRolls += 1
                        if rows[i-1][j] == '@': # above middle
                            adjacentRolls += 1
                        if rows[i-1][j+1] == '@': # above right
                            adjacentRolls += 1

                        if adjacentRolls < 4:
                            rollsAccessible += 1
                            rows[i] = list(rows[i])
                            rows[i][j] = 'x'
                            rows[i] = "".join(rows[i])
                            removed += 1
                            tempList = [i, j]
                            indexes.append(tempList)

                else: # check left, right, above, and below
                    if j == 0: # right, above, below
                        if rows[i][j+1] == '@': # right
                            adjacentRolls += 1
                        if rows[i-1][j] == '@': # above middle
                            adjacentRolls += 1
                        if rows[i-1][j+1] == '@': # above right
                            adjacentRolls += 1
                        if rows[i+1][j] == '@': # below middle
                            adjacentRolls += 1
                        if rows[i+1][j+1] == '@': # below right
                            adjacentRolls += 1

                        if adjacentRolls < 4:
                            rollsAccessible += 1
                            rows[i] = list(rows[i])
                            rows[i][j] = 'x'
                            rows[i] = "".join(rows[i])
                            removed += 1
                            tempList = [i, j]
                            indexes.append(tempList)
                    elif j == (len(rows[i]) - 1): # left, above, below
                        if rows[i][j-1] == '@': # left
                            adjacentRolls += 1
                        if rows[i-1][j-1] == '@': # above left
                            adjacentRolls += 1
                        if rows[i-1][j] == '@': # above middle
                            adjacentRolls += 1
                        if rows[i+1][j-1] == '@': # below left
                            adjacentRolls += 1
                        if rows[i+1][j] == '@': # below middle
                            adjacentRolls += 1

                        if adjacentRolls < 4:
                            rollsAccessible += 1
                            rows[i] = list(rows[i])
                            rows[i][j] = 'x'
                            rows[i] = "".join(rows[i])
                            removed += 1
                            tempList = [i, j]
                            indexes.append(tempList)
                    else: # all 4 directions
                        if rows[i][j-1] == '@': # left
                            adjacentRolls += 1
                        if rows[i][j+1] == '@': # right
                            adjacentRolls += 1
                        if rows[i-1][j-1] == '@': # above left
                            adjacentRolls += 1
                        if rows[i-1][j] == '@': # above middle
                            adjacentRolls += 1
                        if rows[i-1][j+1] == '@': # above right
                            adjacentRolls += 1
                        if rows[i+1][j-1] == '@': # below left
                            adjacentRolls += 1
                        if rows[i+1][j] == '@': # below middle
                            adjacentRolls += 1
                        if rows[i+1][j+1] == '@': # below right
                            adjacentRolls += 1

                        if adjacentRolls < 4:
                            rollsAccessible += 1
                            rows[i] = list(rows[i])
                            rows[i][j] = 'x'
                            rows[i] = "".join(rows[i])
                            removed += 1
                            tempList = [i, j]
                            indexes.append(tempList)

    if rollsAccessible == 0:
        break


print(removed)