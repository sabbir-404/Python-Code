import random

print("===WELCOME===\nGuess the correct 4-digit number.")

num = random.randint(1000, 9999)
print()
n = int(input('Enter your number: '))

if n == num:
    print(f"CONGRATULATIONS!!!\nYou guessed the number {num} in one try, you are indeed a mastermind.")
else:
    guess = 1
    
    while n != num:
        n_str = str(n)
        num_str = str(num)
        digits = ['x'] * 4
        
        for i in range(4):
            if n_str[i] == num_str[i]:
                digits[i] = n_str[i]
        
        print(f"\nYour number didn't match. However, these numbers matched in their positions: {''.join(digits)}\n")
        
        n = int(input("Enter your number again: "))
        while len(str(n)) != 4:
            n = int(input("Enter a 4-digit number: "))
        
        guess += 1

    print(f"Yay!! You guessed the correct number {num}.\nYou needed {guess} tries to become a mastermind.")
