#Rock, paper, scissors
import random
throw = ["Rock", "Paper", "Scissors"]
you_val = 0
comp_val = 0
def Tie():
    print("Tie.")
    print("You: " + str(you_val) + " / Computer: " + str(comp_val) + "\n")
def PlayerWins():
    global you_val
    you_val += 1
    print("You win!") 
    print("You: " + str(you_val) + " / Computer: " + str(comp_val) + "\n")
def CompWins():
    global comp_val
    comp_val += 1
    print("Computer wins.")
    print("You: " + str(you_val) + " / Computer: " + str(comp_val) + "\n")
while True:
    user_input = input("Rock, paper, scissors: ")
    user_input = user_input.capitalize()
    sel = random.choice(throw)
    if user_input == "Rock":
        if sel == "Rock":
            print("You: Rock // Computer: Rock")
            Tie()
        if sel == "Paper":
            print("You: Rock // Computer: Paper")
            CompWins()
        if sel == "Scissors":
            print("You: Rock // Computer: Scissors")
            PlayerWins()
    if user_input == "Paper":
        if sel == "Rock":
            print("You: Paper // Computer: Rock")
            PlayerWins()
        if sel == "Paper":
            print("You: Paper // Computer: Paper")
            Tie()
        if sel == "Scissors":
            print("You: Paper // Computer: Scissors") 
            CompWins()
    if user_input == "Scissors":  
        if sel == "Rock":
            print("You: Scissors // Computer: Rock")
            CompWins()
        if sel == "Paper":
            print("You: Scissors // Computer: Paper")
            PlayerWins()
        if sel == "Scissors":
            print("You: Scissors // Computer: Scissors")
            Tie()