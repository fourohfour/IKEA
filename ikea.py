import random
import urllib.request

def getFurnitureList():
    words = []
    with open("items.txt", "r") as f:
        for i in f:
            words.append(i.strip())

    return words

def AnOrA(ch):
    vowelsstd = ["a", "e", "i", "o", "u"]
    if ch in vowelsstd:
        return "an "
    else:
        return "a "

def getAdjectiveList():
    adjectives = []
    with open("adjectives.txt", "r") as f:
        for i in f:
            adjectives.append(AnOrA(i.strip()[:1]) + i.strip())
    return adjectives

def listAsStr(l):
    p = ""
    for i in l:
        p = p + i.upper()
    return p

def getIkeaProducts(n):
    furniture = getFurnitureList()
    adjectives = getAdjectiveList()
    consonants = {"b" : 50, "c" : 60, "d" : 70, "f" : 40, "g" : 50, "h" : 50, "j" : 30, "k" : 40, "l" : 65, "m" : 70, "n" : 55, "p" : 60, "q" : 20, "r" : 40, "s" : 80, "t" : 75, "v" : 40, "w" : 25, "x" : 5, "y" : 15, "z" : 10}
    vowels = list("aåäeioöu")
    
    for i in range(n):
        length = random.randint(4, 10)
        v = int(length / 3) + random.randint(0, 1)
        if v < 1:
            v = 1
        word = [" "]
        for i in range(length - v):
            while True:
                c = random.choice(list(consonants.keys()))
                if random.randint(0, 99) < consonants[c]:
                    if not c == word[-1]:
                        word.append(c)
                        break

        for i in range(v):
            word.insert(random.randint(1, len(word)), random.choice(vowels))

        print(listAsStr(word[1:]) + ": " + random.choice(adjectives) + " " + random.choice(furniture))
