data = input()

numbers = sorted([char for char in data if char != '+'])
sorted_data = '+'.join(numbers)

print(sorted_data)
