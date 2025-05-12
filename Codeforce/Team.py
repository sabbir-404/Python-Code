c = 0
for i in range(int(input())):
    usr = map(int, input().split())
    if sum(usr) >= 2:
        c += 1

print(c)