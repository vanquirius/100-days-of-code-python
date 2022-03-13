# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-09

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 24 - Mail Merge

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_names():
    with open("Input/Names/invited_names.txt", mode="r") as f:
        names = f.readlines()
        names = [w.replace('\n', '') for w in names]
        print("Name list:")
        print(names)
        return names


def import_starting_letter():
    with open("Input/Letters/starting_letter.txt", mode="r") as f:
        letter = f.read()
        print("Letter format:")
        print(letter)
        return letter

def add_names_to_letters(input_names, input_letter):
    for i in input_names:
        letter_with_name = input_letter.replace("[name]", i)
        outputfile = "./Output/ReadyToSend/" + str(i) + ".txt"
        with open(outputfile, mode="w") as f:
            f.write(str(letter_with_name))

names = read_names()
letter = import_starting_letter()
add_names_to_letters(names, letter)
