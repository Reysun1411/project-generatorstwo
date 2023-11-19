import random

fileName = "russian_nouns.txt"
gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
nouns = []

def req():
    try:
        howmuch = int(input("Сколько проджектов вам сделать? "))
    except ValueError:
        print("Обмануть решил?")
        return False
    if howmuch > 1000:
        print("А ты уверен, что комп выдержит?")
        return False
    elif howmuch < 1:
        print("Ну и сам тогда придумывай проджекты")
        return False
    return howmuch

def reading():
    nounstxt = open(fileName, "r", encoding="utf8")
    return (nounstxt.read()).split("\n")

def projectGenerator(nouns):
    word = random.choice(nouns)

    if word[-1] in gls:
        end = "вство"
    elif word[-1] == "ь":
        word = word[:-1]
        end = "овство"
    else:
        end = "ство"

    return "проджект " + word + end

if __name__ == '__main__':
    while True:
        howmuch = req()
        if howmuch:

            if not nouns:
                nouns = reading()

            print("---")
            for i in range(howmuch):
                print(projectGenerator(nouns))
            print("---")