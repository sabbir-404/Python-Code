import random

words = ['rainbow', 'computer', 'science', 'programming', 'python',
        'mathematics', 'player', 'condition', 'reverse', 'water', 
        'board', 'geeks', 'algorithm', 'database', 'network', 'hardware', 
        'software', 'interface', 'application', 'cybersecurity', 
        'encryption', 'firewall', 'debugging', 'compiler', 'interpreter', 
        'syntax', 'variable', 'function', 'loop', 'array', 'object', 
        'class', 'inheritance', 'polymorphism', 'encapsulation', 
        'abstraction', 'binary', 'decimal', 'hexadecimal', 'octal', 
        'bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 
        'petabyte', 'exabyte', 'zettabyte', 'yottabyte']


word = random.choice(words)

print('===WELCOME===')
print()
print("Guess the characters\nYou have 20 chances only, for every wrong word your chance will reduce.")

guesses = ''
turns = 20

while turns > 0:
    word_position = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            word_position += 1

    if word_position == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("\nWrong")
        print(f"You have {turns} more guesses")
        if turns == 0:
            print(f"You Loose\nWord is :{word}")

k = input("Press enter to close")