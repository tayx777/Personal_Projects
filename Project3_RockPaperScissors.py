import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]



while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue # asks them to enter a valid entry rather than printing an "Error" code if the input is not in the list
                 # will keep asking them to enter something in until we get a valid response (rock/paper/scissors/q)

    random_number = random.randint(0,2)    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")


#Option 1 of writing this code WITH elif statements:
    if user_input == computer_pick:
        continue

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")


#Option 2 of writing this code WITHOUT elif statements:
    #if user_input == "rock" and computer_pick == "scissors":
    #    print("You won!")
    #    user_wins += 1
    #    continue

    #if user_input == "paper" and computer_pick == "rock":
    #    print("You won!")
    #    user_wins += 1
    #    continue

    #if user_input == "scissors" and computer_pick == "paper":
    #    print("You won!")
    #    user_wins += 1
    #    continue


print("Goodbye!")