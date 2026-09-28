import random
print("Welcome to the Higher/Lower Game")

solution = random.randiant(1,100)

#Get and avlidate user input
guess = int(input("Guess a number between 1 and 100"))
while guess > 100 or guess < 1:
    guess = int(input("Guess a number between 1 and 100"))

#Determine the result 
if guess > solution:
    print("Lower")
elif guess < solution:
    print("Higher")
else:
    print("")