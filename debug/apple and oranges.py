c = 0
n = 5
for i in range(1,(n + 2), 5):
    if i % 5 == 0 or i % 10 == 0:
        c += 1
        
print(c)