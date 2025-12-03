with open("input.txt", "r") as file:
    content = file.read()
    ranges = content.split(",")

invalid = []
for currentRange in ranges:
    temp = currentRange.split("-")
    start = int(temp[0])
    end = int(temp[1]) + 1
    for i in range(start, end): # find repeated substring (rep 2x)
        strI = str(i)
        if len(strI) % 2 != 0: # length not even
            continue

        middleIndex = int(len(strI) / 2)
        if strI[:middleIndex] == strI[middleIndex:]:
            # add invalid to array
            invalid.append(i)


# sum up array
answer = sum(invalid)
print(answer)