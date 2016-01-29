import random
number = random.randint(1,100)
def guessAgain():
        i = input("Again? y/n ")
        i = i.lower()
        if i == "y":
                return True
        elif i == "n":
                return False
        else:
                print("I don't understand? Try y or n.")
                return None
print("I'm thinking of a number between 1 and 100.")
play = True
count = 0
while play == True:
        try:
                guess=int(input("Guess what it is? "))
        except ValueError:
                print("I said I was thinking of a *number*")
                continue
        count+=1
        if guess > 100 or guess <1:
                print("You aren't even trying")
        elif guess < number:
                print("Too low")
        elif guess > number:
                print("That is too high!")
        elif guess == number:
                print("You guessed it! It took you "+str(count)+" guesses.")
                count = 0
                number = random.randint(1,100)
                play = None
                while play == None:
                        play = guessAgain()
