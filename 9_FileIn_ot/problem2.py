# The game() function in a program lets a user play a game and returns the score as an interger. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random
def game():
    print("Welcome to the game!")
    score = random.randint(1, 500)  # Simulating a game score
    with open("D:\\python\\9_FileIn_ot\\Hi-score.txt") as file:
        hiscore = file.read()
        if hiscore.isdigit():
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your current score is: {score}")
    if(score>hiscore ):
       with open("D:\\python\\9_FileIn_ot\\Hi-score.txt", "w") as file:
           file.write(str(score))
    return score

game()