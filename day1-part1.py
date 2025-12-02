with open("input.txt", "r") as file:
    content = file.read()
    steps = content.split("\n")

current = 50 # starts at 50
times = 0

for step in steps:
    print(f"Step: {step}")
    if step[0] == 'R':
        current += int(step[1:])
        print(f"left: {current}")
        # if > 99
        if current > 99:
            current = current % 100
    elif step[0] == 'L':
        current -= int(step[1:])
        print(f"right: {current}")
        # if negative
        if current < 0:
            current = (current + 100) % 100;
    else:
        continue
    
    # check if ends at 0
    if current == 0:
        times += 1
        print(times)

print(times)