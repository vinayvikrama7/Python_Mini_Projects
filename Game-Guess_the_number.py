
import random

upper_limit=input("enter the upper limit integer to generate random number: ")

print("\n")

#for i in range(1):

if (upper_limit.isdigit()):
    upper_limit=int(upper_limit)
else:
    upper_limit=input("please enter a valid integer: ")
    if (upper_limit.isdigit()):
        upper_limit=int(upper_limit)
    else:
        print("Next time enter a valid integer")
        quit()

print("upper limit = "+str(upper_limit))
random_num = random.randint(1, upper_limit)
print("generating random number ================= > Generated\n")


num_of_guesses=0

while True:
    num_of_guesses=num_of_guesses+1
    guess=input("Guess the random number generated: ")
    if (guess.isdigit()):
        guess=int(guess)
    else:
        print("Next time enter a valid integer")
        continue
    if(guess>random_num):
        print("The generated random number is less than the number you guessed")
        
    elif(guess<random_num):
        print("The generated random number is greater than the number you guessed")
        
    else:
        print("Correct!!! That is the generated random number")
        break

print("You guessed it in", num_of_guesses, "guesses")