import random

top_range = input("Type a number for top of range: ")

# create parameters for the user input. Ensure they input a number or exit the program. 
if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please provide a number greater than 0 next time. ")
        quit()
else:
    print("Please type a number next time. ")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

# create a while loop that only breaks when users guesses correct number
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue
     
    if user_guess == random_number:
        print("You got it right! ")
        break
    elif user_guess > random_number:
        print("Keep Guessing! Try lower... ")
    else:
        print("Keep Guessing! Try higher... ")

# create output once the user has broken the loop
if guesses == 1:
    print("It took you " + str(guesses) + " guess to get the right answer. You're a rockstar!")
else:
    print("It took you " + str(guesses) + " tries to get the right answer: " + str(random_number))
