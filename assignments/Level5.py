import random

#here we need to check the remainder of number user input to say whether it's odd or even
num_round = int(input("How many arounds do you wanna play"))
while num_round%2 == 0 or num_round < 0:
    num_round = int(input("Sorry, the number must be an odd number. Please try again:"))


#now we have to return the value we need, which is num_round,it should be out of while loop
def get_player_choice():
    player_choice = input('Enter rock, paper, scissors: ').lower()
    while player_choice not in answers:
        print(f"Sorry, “{player_choice}” is not a valid choice. Please try again.\n")
        player_choice = input('Enter rock, paper, scissors: ').lower()
    return player_choice

#this function is used to vertify which who can win the game
def determine_winner(player_choice, computer_choice):
    #there are many ways to do it, here I choose to use the function of dictionary i learnt from another school, you can also list all thoes posibility, or may be give them numbers to campare each other.
    winning_dict = {
        "rock": "scissors",  
        "scissors": "paper",   
        "paper": "rock"
    }
    if computer_choice == player_choice:
        print("Tie! Play again.") 
        result = 'tie'
    elif winning_dict[player_choice] == computer_choice:
        print("You won!")
        result = "win"
    else:
        print("You lost!")
        result = "lose"
    return result



#This part we need to connect to functions into one main functiuon
print("Welcome to Rock Paper Scissors!")
r = 0     
wining_points = 0
losing_points = 0
answers = ['rock', 'paper', 'scissors']

while r != num_round:

    user_answer = get_player_choice()

#This code is used for letting computer generate a code for us
    computer_choice_num = random.randint(0,2)
    computer_choice = answers[computer_choice_num]
    print(f"The computer chose {computer_choice}")

    a = determine_winner(user_answer, computer_choice)

    r += 1 #every circle, r will be added one, until the round is same to the rounds the player want to play

    if a == "tie":
        r -= 1 #because we have to play again, so this round doen't count, we should deduct this round from total rounds.
    elif a =="lose":
        losing_points += 1 
    else:
        wining_points += 1
#this part is just summary, really easy
print("------------------------------")
print(f"Score: You: {wining_points} | Computer: {losing_points}\n")

if wining_points > losing_points:
    print("You won!\nThans for playing")
else:
    print("You lose\nThans for playing!")








