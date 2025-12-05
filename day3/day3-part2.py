with open("input.txt", "r") as file:
    content = file.read()
    banks = content.split("\n")

maxJoltages = []
outputLength = 12

def getMax(bank, start, end):
    max = 0
    index = 0
    for i in range(start, end+1):
        if int(bank[i]) > max:
            max = int(bank[i])
            index = i
    return index


for bank in banks: # loop through banks/lines
    digitsNeeded = outputLength - 1
    joltage = []
    currX = 0
    for i in range(0, outputLength): # repeat 12 times
        endIndex = len(bank) - (outputLength - len(joltage)) # length of given input - (needed length - length already added)
        index = getMax(bank, currX, endIndex)
        joltage.append(bank[index])
        digitsNeeded -= 1
        currX = index + 1

    joltageStr = "".join(joltage)
    maxJoltages.append(int(joltageStr))


answer = sum(maxJoltages)
print(answer)