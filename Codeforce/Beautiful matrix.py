data = []
rcrd = 1
cond = False
for i in range(5):
    usr_inpt = [int(x) for x in input().split()]
    if 1 not in usr_inpt and cond == False:
        rcrd += 1
    elif 1 in usr_inpt:
        cond = True
    data.append(usr_inpt)

column = rcrd 
steps = 0       

while column != 3:
    if column < 3:
        column += 1
    elif column > 3:
        column -= 1
    steps += 1

row = (data[rcrd - 1].index(1)) + 1

while row != 3:
    if row < 3:
        row += 1
    elif row > 3:
        row -= 1
    steps += 1

print (steps)