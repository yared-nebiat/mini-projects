import random

print("Guess a number between 1 and 10 inclusive.")
retry = True

while retry:
    num = random.randint(1, 10)
    guess_limit = 3
    guess_count = 0
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        if guess == num:
            print("You win!")
            break
        else:
            print("Wrong!")
        guess_count += 1
    else:
        print("The number was",num)
    if input("Again?\n(y)/(n)\n") == 'n':
        retry = False
