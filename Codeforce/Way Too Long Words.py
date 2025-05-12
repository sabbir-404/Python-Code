def word_short_form(word):
    if len(word) <= 10:
        print(word)
    else:
        tmp = word[0] + str(len(word) - 2) + word[-1]
        print(tmp)

for i in range(int(input())):
    word_short_form(input())