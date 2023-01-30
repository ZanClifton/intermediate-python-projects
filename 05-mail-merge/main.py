with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

    with open("./Input/Names/invited_names.txt") as invited_names:
        names = invited_names.readlines()
        for name in names:
            new_name = name.strip("\n")
            new_letter = letter.replace("[name]", new_name)
            print(new_letter)
