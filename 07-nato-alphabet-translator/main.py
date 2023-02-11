import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    # print(key, value)
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    # print(row.student, row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

reference_dict = {row.letter: row.code for (
    index, row) in nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_needs_words_translating = "y"

while user_needs_words_translating != "n":

    user_word = input("What word would you like to translate? ")

    new_array = [reference_dict[letter.upper()] for letter in user_word]

    print(new_array)

    user_needs_words_translating = input(
        "Would you like to translate another word? y/n ").lower()
