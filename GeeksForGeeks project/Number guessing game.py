import random
import math

lower = int(input("Enter lower Value: "))
upper = int(input("Enter upper Value: "))

x = random.randint(lower, upper)
chances = math.ceil(math.log(upper - lower + 1, 2))

print(f"\nYour range is {lower} to {upper}, you only have {chances} chances left.")

c = 0
tmp = chances
flag = False
while c <= chances:
    user = int(input("\nEnter your Number: "))
    if user > x:
        tmp -= 1
        print(f"{user} is too high, try smaller. You have {tmp} chances left.")
        c += 1
    elif user < x:
        tmp -= 1
        print(f"{user} is too low try higher number. You have {tmp} chances left.")
        c += 1
    elif user == x:
        print(f"{user} is the correct answer\nYou got the answer in {chances - tmp}.")
        flag = True
        break
    
if not flag:
    print(f"\nYou have exceeded the number of chances!\nThe number is {x}\nBetter luck next time!!")

k = input("Press Enter to close.")