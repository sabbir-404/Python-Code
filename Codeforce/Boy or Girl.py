def determine_gender(username: str):
    unique_chars = set(username)  
    if len(unique_chars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

username = input()
determine_gender(username)
