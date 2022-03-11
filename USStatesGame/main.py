# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 25 - US States Game

ALIGN = "center"
FONT = ('Arial', 20, 'normal')

import turtle
import pandas
from statename import Statename

screen = turtle.Screen()
screen.title = ("US States Game")
# Load empty map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import State list
def import_state_list():
    datasource = "50_states.csv"
    df = pandas.read_csv(datasource)
    # print("Imported data:")
    # print(df)
    return df

# Prompt user for State
def prompt_user_state(input_df):
    try:
        input_title = str(score) + "/50 correct"
        answer_state = screen.textinput(title=input_title, prompt="What's a valid state").title()
    except:
        answer_state = ""
    print("Answer was: " + str(answer_state))
    # Returns true or false if the answer was correct
    if answer_state == "Exit":
        return answer_state, ""
    return any(df.state == answer_state), answer_state

# Write State on screen
def write_state_on_screen(input_df, input_state):
    statelist = input_df[input_df.state == input_state]
    # print(statelist)
    x = statelist.iloc[0]['x']
    y = statelist.iloc[0]['y']
    statename = Statename(input_state, x, y)
    output_df = input_df.drop(input_df[input_df.state == input_state].index)
    return output_df

df = import_state_list()

game_is_on = True
score = 0
answer = ""

while game_is_on:
    if answer == "Exit":
        df.to_csv("missed_states.csv")
        break
    answer, state = prompt_user_state(df)
    if answer is True:
        score += 1
        df = write_state_on_screen(df, state)