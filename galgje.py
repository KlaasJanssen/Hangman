import random
import os
import gallow
import time
import taal

def import_words(word_file):
    f = open(word_file)
    words = []
    for line in f:
        splitted_line = line.strip("\n").split("\t")
        words.append(splitted_line[0])
    return words

def check_valid(letter, guesses):
    if letter.lower() in guesses:
        valid = False
        reason = texts["already_guessed"]
    elif not len(letter) == 1:
        valid = False
        reason = texts["not_1_letter"]
    elif not letter.isalpha():
        valid = False
        reason = texts["not_a_letter"]
    else:
        valid = True
        reason = ""
    return valid, reason

def check_letter(letter, word, guessed, mistakes):
    if letter in word:
        i = 0
        guess_temp = list(guessed)
        for letters in word:
            if letters == letter:
                guess_temp[i] = letter
            i += 1
        guessed = "".join(guess_temp)
    else:
        mistakes += 1
    return guessed, mistakes

def check_game_end(word, guessed, mistakes):
    if guessed == word:
        cont = False
        text = texts["won"]
    elif mistakes == 10:
        cont = False
        text = texts["lost"].format(word)
    else:
        cont = True
        text = ""
    return cont, text

def continue_game():
    valid_answer = False
    while not valid_answer:
        cont = input(texts["cont"])
        if cont.upper() == texts["yes"]:
            valid_answer = True
            game = True
        elif cont.upper() == "N":
            valid_answer = True
            game = False
        else:
            print(texts["invalid_continue"])
    return game


if __name__ == "__main__":
    texts = taal.language_set()
    print(texts["word_file"])
    words = import_words(texts["word_file"])
    gallows = gallow.construct_gallow()
    game = True

    while game:
        word = random.choice(words)
        guessed = "-" * len(word)
        alive = True
        mistakes = 0
        guesses = []
        while alive:
            os.system("cls")
            #print(word)
            print(gallows[mistakes], "\n\n", guessed)
            letter = input(texts["select_letter"])
            if letter == "stop":
                game = False
                alive = False
            valid, reason = check_valid(letter, guesses)
            if not valid:
                print(reason)
                time.sleep(2)
            else:
                guesses.append(letter)
                guessed, mistakes = check_letter(letter, word, guessed, mistakes)
                alive, text = check_game_end(word, guessed, mistakes)
                if not alive:
                    os.system("cls")
                    #print(word)
                    print(gallows[mistakes], "\n\n", guessed)
                    print(text)
                    game = continue_game()
