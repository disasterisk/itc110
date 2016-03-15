#! python3

import random
coin = ['heads', 'tails']
toss = str(random.choice(coin))
guess = input('heads or tails?\n')
while guess not in coin:
    print("Sorry, I don't understand.")
    guess = input('heads or tails?\n')
win = 'That was it!'
if toss == guess:
    print(win)
else:
    print("That wasn't it! Guess again.")
    guess = input('heads or tails?\n')
    while guess not in coin:
        print("Sorry, I don't understand.")
        guess = input('heads or tails?\n')
    if toss == guess:
        print(win + " I was worried there for a second.")
    else:
        print("Congratulations! You have redefined failure.")
