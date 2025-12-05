with open("input.txt", "r") as file:
    content = file.read()
    banks = content.split("\n")

maxJoltages = []

for bank in banks: # loop through banks/lines
    largest = 0
    bankStr = str(bank)
    for i in range(0, (len(bankStr) - 1)):
        for j in range(i+1, len(bankStr)):
            temp = str(bank[i]) + str(bank[j])
            if int(temp) > largest:
                largest = int(temp)
    maxJoltages.append(largest)


answer = sum(maxJoltages)
print(answer)
