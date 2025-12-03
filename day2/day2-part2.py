with open("input.txt", "r") as file:
    content = file.read()
    ranges = content.split(",")

invalid = []
for currentRange in ranges:
    temp = currentRange.split("-")
    start = int(temp[0])
    end = int(temp[1]) + 1
    for i in range(start, end):
        strI = str(i)
        if (strI + strI).index(strI, 1) < len(strI):
            # add invalid to array
            invalid.append(i)


# sum up array
answer = sum(invalid)
print(answer)