# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-05-07

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 81 - Text to Morse Code Converter

# You will use what you've learnt to create a text-based (command line) program
# that takes any String input and converts it into Morse Code.

# Wikipedia for Morse Code
# https://en.wikipedia.org/wiki/Morse_code

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Capture keyboard input from user
def capture_input() -> str:
    string_input = str(input("Enter your message here:").upper())
    return string_input


# Convert a text string to morse
def text_to_morse(input_text) -> str:
    morse_message = ""
    for i in input_text:
        if i in MORSE_CODE_DICT:
            morse_message += str(MORSE_CODE_DICT.get(i)) + " "
        else:
            print("Warning: character not in dictionary")
            morse_message += i
    print("In morse:")
    print(morse_message)
    return morse_message


string = capture_input()
text_to_morse(string)
