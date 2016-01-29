import random
dic1 = ["life", "moon", "butter", "fire", "basket", "foot", "weather", "earth", "play", "super", "grand", "rattle", "skate", "grass", "eye", "honey", "dish", "pop", "book", "thunder", "head", "glass", "boot", "air", "baby", "ham", "common", "sea", "sand", "river", "tooth", "town", "sauce", "disk", "horse", "rain", "stone"] # - week, no, north, up, down, more, along, cross, some, back, home, every, what, long, school, watch, key, under, south, any, life, black, wide, rail
dic2 = ["guard", "walk", "time", "light", "body", "flies", "thing", "ball", "man", "quake", "stream", "day", "bone", "giant", "goat", "mother", "flower", "structure", "snake", "board", "house", "hopper", "made", "smith", "moon", "washer", "corn", "case", "fish", "storm", "town", "maker", "making", "plane", "sitter", "person", "ship", "dew", "drive", "paste", "keeper", "check", "woman","watch", "fighter"]#-ever, self, place, pan, back, down, way, shore, pick, noon, end, stone, ground, drive, road, strap
goodWords = set()
end = "Maybe another time then"
print ("Want to know my favorite word?")
def ask():
    ans = input('y/n: ')
    if ans == 'y':
        return True
    else:
        return False
play = ask()
while play == True :
    corn = random.choice(dic1)
    dog = random.choice(dic2)
    cornDog=corn+dog
    if len(goodWords)<(len(dic1)*len(dic2)):
        while cornDog in goodWords:
            print ("Hold on...")
            corn = random.choice(dic1)
            dog = random.choice(dic2)
            cornDog=corn+dog
        goodWords.add(cornDog)
        print (("\'"+cornDog+".\' ")+(cornDog+" ")*random.randint(2,4)+cornDog+".")
        print ("Do you want to hear another excellent word?")
        play = ask()
    else:
        end = "There are no more! Are you happy??"
        play = False
print (end)
