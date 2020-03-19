#higher lower guessing game
import random
r = random.randint(1, 101)
counter = 0
while True:
    user_num = int(input("Pick a number between 1 and 100: "))
    if user_num > r:
        print("Lower!" + "\n")
        counter += 1
    elif user_num < r:
        print("Higher!" + "\n")
        counter += 1
    elif user_num == r:
        print("Congrats! You guessed the correct number in " + str(counter) + " guesses.") 
        user_q = input("Do you want to play again?(Y/N): " + "\n")
        user_q = user_q.capitalize()
        if user_q == "Y":
            r = random.randint(1, 101)
            counter = 0
            continue
        else:
            exit()      