import random
import string
import time
import datetime
from PyDictionary import PyDictionary
from english_words import english_words_lower_alpha_set
from itertools import permutations


def main():
    target = generate()
    print("Letters to choose from: " + target)
    print("Get ready!")
    timer(3, False)
    print("Here's the Countdown clock...")
    timer(10, print)
    print("Time's up!")

    one_in = input("Player one's word: ")
    two_in = input("Player two's word: ")

    one = is_word(one_in.upper(), target)
    two = is_word(two_in.upper(), target)

    if len(one) > len(two):
        print("Player one wins!")
    elif len(two) > len(one):
        print("Player two wins!")
    elif len(one) == 0 and len(two) == 0:
        print("Nobody wins!")
    else:
        print("It's a tie!")

    opt = random.choice(list(corner(target)))
    dictionary = PyDictionary()
    if not dictionary.meaning(opt, disable_errors=True):
        print("There aren't any better words!")
    elif opt == one_in.lower() or opt == two_in.lower():
        print("Good word!")
    else:
        print(f"From Dictionary Corner we also have: {opt}")
        print(dictionary.meaning(opt))


def generate():
    vowels = ["A", "E", "I", "O", "U"]
    alphabet = list(string.ascii_uppercase)
    consonants = [x for x in alphabet if x not in vowels]

    choices = []
    while len(choices) < 9:
        ask = input("Consonant or a vowel? ").casefold()
        if ask == "consonant" or ask == "c":
            choices.append(random.choice(consonants))
        elif ask == "vowel" or ask == "v":
            choices.append(random.choice(vowels))
        else:
            print("Please pick 9 consonants and vowels")
    return "".join(choices)


def timer(duration, print=True):
    while duration > 0:
        time_left = datetime.timedelta(seconds=duration)
        if print:
            print(time_left, end="\r")
        time.sleep(1)
        duration -= 1


def checker(word):
    dictionary = english_words_lower_alpha_set
    if word.lower() in dictionary:
        return True
    else:
        return False


def is_word(word, target):
    if checker(word) == False:
        print(f"{word} is not an English word")
        return ""
    chars = [*word]  # split string into list of chars
    target = [*target]
    for letter in chars:
        try:
            target.remove(letter)
        except ValueError:
            print(f"{word} is not made from the given letters")
            return ""
    return word


def corner(t):
    dictionary = english_words_lower_alpha_set
    t = t.lower()
    list = []
    for i in range(1, 10):
        for target in permutations(t, i):
            target = "".join(target)
            list.append(target)

    possibles = [x for x in list if x in dictionary]

    longs = []
    possibles = sorted(possibles, key=len)
    for length in possibles:
        if len(length) == len(possibles[-1]):
            longs.append(length)

    return set(longs)


if __name__ == "__main__":
    main()
