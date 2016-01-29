import random
nouns = ["an orange","a microphone","a remote control","a kindergarten","the police"]
funny = True
def parse(x):
    stripped = ''.join(filter(str.isalpha, x))
    return stripped.lower()
while funny == True:
    response = parse(input("Knock, knock. "))
    if response == "whosthere":
        hilariousNoun = random.choice(nouns)
        while funny == True:
            response = parse(input(hilariousNoun.capitalize()+". "))
            who = hilariousNoun.capitalize()+" who?"
            if response == parse(who):
                print(hilariousNoun.capitalize()+" is at your door! What a crazy, random happenstance! Are you not amused!?")
                funny = False
            else:
                print("You are supposed to say, '"+who+"'!")
                continue
    else:
        print("You're supposed to say 'who's there?'!")
        continue
