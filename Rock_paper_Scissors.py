import random
from time import sleep

choice = ["rock","paper","scissors"]
computer = random.choice(choice)

player = False

while player == False:
    print("Welcome to Rock,paper and Scissors")
    print("\nplease wait the game is loading")
    sleep(3)
    player = input("Which one do you want to choose?\n'Rock': 'Rock'\n'Paper': 'Paper'\n'Scissors': 'Scissors'\n'Stop the game': 'Stop': ")
    if player == computer:
        print("\nPlease wait we are loading your results....")
        sleep(2)
        print("It is a Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("\nPlease wait we are loading your results....")
            sleep(2)
            print("you have lost!!")
        else:
            print("\nPlease wait we are loading your results....")
            sleep(2)
            print("you have won!!")

    elif player == "scissors":
        if computer == "rock":
            print("\nPlease wait we are loading your results....")
            sleep(2)
            print("you have lost!!")
        else:
            print("\nPlease wait we are loading your results....")
            sleep(2)
            print("you have won!!")

    elif player == "paper":
        if computer == "scissors":
           print("\nPlease wait we are loading your results....")
           sleep(2)
           print("You have lost!!")
        else:
           print("\nPlease wait we are loading your results....")
           sleep(2)
           print("you have won!!")

    elif player == "stop":
        print("Thanks for playing")
        break

    else:
        print("That's not a valid play!!")
        break

    player = False
