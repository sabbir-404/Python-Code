s, t = (input().split())
a, b = (input().split())
m, n = (input().split())
a_fruit = list(map(int, input().split()))
b_fruit = list(map(int, input().split()))

res_a = []
for fruit in a_fruit:
    res_a.append(fruit + int(a))
    

res_b = []
for fruit in b_fruit:
    res_b.append(fruit + int(b))

c_a = 0
c_b = 0

for val in res_a:
    if int(s)<= val <=int(t):
        c_a += 1

for val in res_b:
    if int(s)<= val <=int(t):
        c_b += 1

print(c_a)
print(c_b)
