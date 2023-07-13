from random import randint

opt = ["rock", "paper", "scissors"]

print("First to 3 wins is the winner\n")


def winner(comp, usr):
    if (comp == 'rock' and usr == 's') or (comp == 'paper' and usr == 'r') or (comp == 'scissors' and usr == 'p'):
        return comp
    elif (usr == 'r' and comp == 'scissors') or (usr == 'p' and comp == 'rock') or (usr == 's' and comp == 'paper'):
        return usr
    else:
        return 0


play_again = True

while play_again:
    count = 0
    usr_win_count = 0
    comp_win_count = 0
    while usr_win_count < 3 and comp_win_count < 3:

        computer = opt[randint(0, 2)]
        user = input("Enter rock, paper or scissors: ")
        if len(user) != 0:
            user = user[0].lower()

        print("You:", user, '\t\t\t\t\t\t\t\t\t', "Computer:", computer)

        if winner(computer, user) is computer:
            comp_win_count += 1
        elif winner(computer, user) is user:
            usr_win_count += 1
        else:
            print("\t\t\t\t\t\tDraw")
        print("\t\t\t\t\t\tScores\n\t\t\tYou:", usr_win_count, "\t\t\t\t\t\tComputer:", comp_win_count)
        if usr_win_count == 3:
            print("\t\t\t\t\t\tYou won!")
        elif comp_win_count == 3:
            print("\t\t\t\t\t\tYou lost")

    if input("\nPlay again?\n(y)/(n)\n") == 'n':
        play_again = False
