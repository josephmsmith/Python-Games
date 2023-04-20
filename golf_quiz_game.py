# first create a virtual environment to run the game :) 
import time

print('Welcome to my golf quiz!')   #intro to game

playing = input('Do you want to play? ') 
if playing == "yes":
    time.sleep(1)
    print('\nOkay! Lets get going then... : ) ')
else:
    print('\n\nBummer, see you next time!\n')
    quit()

score = 0   #form a scoring mechanism

time.sleep(1)
answer = input("\nHow many holes are there on a golf course typically? ")
if answer.lower() in ["18", "eighteen"]:
    print("correct!\n")
    score += 1
else:
    print('false, it is 18\n')

answer = input("What does GIR stand for? ")
if answer.lower() in ["Greens in regulation", "greens in regulation"]:
    print("correct!\n")
    score += 1
else:
    print('false, it is greens in regulation\n')

answer = input("How many times has Tiger Woods won The Masters? ")
if answer.lower() in ["5", "five"]:
    print("correct!\n")
    score += 1
else:
    print('false, the answer is 5 times\n')

answer = input("Which major has Rory McIlroy not won? ")
if answer.lower() in ["the masters", "masters"]:
    print("correct!\n")
    score += 1
else:
    print('false, it was the masters\n')

answer = input("Which player has won the most major championships in his career? (18) ")
if answer.lower() in ["jack nichlaus", "jack"]:
    print("correct!\n")
    score += 1
else:
    print('false, it was Jack Nichlaus\n')

answer = input("Tiger Woods was born in which US state? ")
if answer.lower() in ["ca", "california"]:
    print("correct!\n")
    score += 1
else:
    print('false, CA\n')

answer = input("The 11th, 12th and 13th holes at Augusta National are collectively known by what nickname? ")
if answer.lower() == "amen corner":
    print("correct!\n\n")
    score += 1
else:
    print('false, it is amen corner\n\n')

print('Wow. You got ' + str(score) + ' out of 7 questions correct.')
print('Thats ' + str(round(score/7*100,2))+ '%')
print('Thanks for playing! ')