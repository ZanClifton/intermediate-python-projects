import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

reference_dict = {row.letter: row.code for (
    index, row) in nato_alphabet.iterrows()}

user_needs_words_translating = "y"

while user_needs_words_translating != "n":

    user_word = input("What word would you like to translate? ")

    try:
        new_array = [reference_dict[letter.upper()] for letter in user_word]
        print(new_array)
    except KeyError:
        print("That's an invalid input. Letters from the alphabet only, please.")

    user_needs_words_translating = input(
        "Would you like to translate another word? y/n ").lower()
