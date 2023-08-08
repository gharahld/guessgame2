import random
import datetime

from db import save_record, print_score


def number_guess():
    counter = 1
    correct_number = random.randint(1, 10)
    user_name = input("What is your name")
    print(f"Hello {user_name} let's play a game...")
    print("Guess a number from 1 to 10")

    while True:
        try:
            guess = int(input())
        except ValueError:
            print("Please use an actual number")
            continue

        if guess != correct_number:
            print("Wrong number, please try again")
            counter += 1
        else:
            print(f"Correct{user_name} you guessed it {counter} time(s)")
            break
    time_of_day = datetime.datetime.now()
    print("Do you want to save your score (Y/N)")
    answer = input()
    if answer == "Y":
        save_record(user_name, counter)
        print("Your score has been saved", (time_of_day.strftime("%b,%d,%Y,%I,%M,%S,%p")))
    elif answer == "N":
        print("your score will not be saved")
    print("Do you want to play the game again?")
    answer2 = input()
    if answer2 == "P":
        print("playing")
    elif answer2 == "L":
        print_score()



if __name__ == '__main__':
    number_guess()
