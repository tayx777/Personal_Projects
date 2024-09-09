import random

# " random " is a default module with Python that generates random values

#r = random.randrange(-5,11) --- only prints values from -5 to 10, and excludes 11 or the "stop" value.
#print(r)

#random.randrange(11) is also an acceptable syntax; prints all values from 0 to 10

#rand = random.randint(9,11) --- " .randint " prints all values from the start to the stop; includes 9, 10, AND 11
#print(rand)


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")

print("You got it in", guesses, "guesses")