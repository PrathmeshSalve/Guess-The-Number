import random
from art import logo
print(logo)
random_num = random.choice(range(1,100))

def easy():
    attempts = 10
    while attempts > -1 :
        print(f"\nYou Have {attempts} Attempts Remaning To Guess The Number.")
        if attempts == -1:
            print("You Lose, Attempts are Over.")
            return
        guess = int(input("Make a guess : "))
        if guess < random_num:
            print("Too Low.")
            if guess != random_num and attempts > 1:
                print("Guess again.\n")
        elif guess > random_num:
            print("Too High.")
            if guess != random_num and attempts > 1:
                print("Guess again.\n")
        else:
            print(f"\nYOU FOUND THE NUMBER : {random_num} YOU WON!!\n")
            return
        attempts -= 1
    return 

def hard():
    attempts = 5
    while attempts > -1 :
        print(f"\nYou Have {attempts} Attempts Remaning To Guess The Number.")
        if attempts == 0:
            print("YOU LOSE")
            return
        guess = int(input("Make a guess : "))
        if guess < random_num:
            print("Too Low.")
            if guess != random_num and attempts > 1:
                print("Guess again.\n")
        elif guess > random_num:
            print("Too High.")
            if guess != random_num and attempts > 1:
                print("Guess again.\n")
        else:
            print(f"\nYOU FOUND THE NUMBER : {random_num} YOU WON!!\n")
            return
        attempts -= 1
    return 

print("Number Is Between 1 to 100")
condition = input(("Choose a difficulty | 'easy' OR 'hard' | : ").lower())
if condition == "easy":
    easy()  # Call the 'easy' function
elif condition == "hard":
    hard()  # Call the 'hard' function
else:
    print("Invalid input. Please retry and choose | 'easy' OR 'hard' |")