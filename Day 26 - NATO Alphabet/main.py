# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-11

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 26 - NATO Alphabet

import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

# Import NATO dictionary into a list
def import_nato_dictionary():
    datasource = "nato_phonetic_alphabet.csv"
    df = pandas.read_csv(datasource)
    dict = {row.letter:row.code for (index, row) in df.iterrows()}
    return dict

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def convert_word_nato_dictionary(input_nato_dict):
    input_word = str(input("Which word to convert to NATO Alphabet?")).upper()
    letter_list = list(input_word)
    output_list = [input_nato_dict[letter] for letter in input_word]
    print(output_list)

nato_dict = import_nato_dictionary()
convert_word_nato_dictionary(nato_dict)