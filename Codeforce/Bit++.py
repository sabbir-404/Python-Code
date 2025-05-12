def bit(instruction, val):
    if '+' in instruction:
        return val + 1
    elif '-' in instruction:
        return val - 1
    return val 

initial = 0
for i in range(int(input())):
    ins = input()
    initial = bit(ins, initial)

print(initial)
