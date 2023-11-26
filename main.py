import random
import os
import game_logo
import game_database
print(game_logo.logo)
score = 0

def display_account_data(account):
    name = account['name']
    description = account['description']
    location = account['location']
    return f"{name}, {description}, {location}"


def check_answer(guess, followers_1, followers_2):
    if followers_1 < followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
           return False


account_2 = random.choice(game_database.candidates_data)
continue_flag = True

while continue_flag:
    account_1 = account_2
    account_2 = random.choice(game_database.candidates_data)
    while account_1 == account_2:
        account_2 = random.choice(game_database.candidates_data)
    print(f"Compare 1: {display_account_data(account_1)}", game_logo.vs,
          f"Compare 2: {display_account_data(account_2)}")
    guess = int(input("\n Who has more followers? Type '1' or '2': "))
    followers_count_1 = account_1['followers_count']
    followers_count_2 = account_2['followers_count']
    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    os.system('cls')
    print(game_logo.logo)
    if is_correct:
        score += 1
        print(f"You're right. Your score is {score}")
    else:
        print(f"You're wrong. Your final score is {score}")
        continue_flag = False
