def language_set():
    valid = False
    while not valid:
        language = input("Select your language (NL/EN): ")
        if language.upper() == "EN":
            texts = {
            "already_guessed":"You have already guessed this letter.",
            "not_1_letter":"Please sumbit exactly 1 letter.",
            "not_a_letter":"You entered a character that is not a letter.",
            "won":"You have won! Do you want to play again?",
            "lost":"You have lost! The word was: {}. Do you want to try again?",
            "cont":"(Y/N): ",
            "yes":"Y",
            "invalid_continue":"Your response has not been recognized, please enter either Y (Yes) or N (No)",
            "select_letter":"Enter a letter: ",
            "word_file":"wordsEN.txt"
            }
            valid = True
        elif language.upper() == "NL":
            texts = {
            "already_guessed":"Je hebt deze letter al geprobeerd.",
            "not_1_letter":"Voer precies 1 letter in.",
            "not_a_letter":"Je hebt een teken ingevoerd dat geen letter is.",
            "won":"Je hebt gewonnen! Wil je nog een keer spelen?",
            "lost":"Je hebt verloren! Het woord was: {}. Wil je het nog een keer proberen?",
            "cont":"(J/N): ",
            "yes":"J",
            "invalid_continue":"Je antwoord werd niet herkend, voer J (Ja) of N (Nee) in",
            "select_letter":"Voer een letter in: ",
            "word_file":"wordsNL.txt"
            }
            valid = True
    return texts
