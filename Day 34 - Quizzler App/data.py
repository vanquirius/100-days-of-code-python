# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-03-20

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 34 - Quizzler App

import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

def get_questions_opentdb():
    # Get random questions from the Open Trivia Database
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    questions = data["results"]
    return questions

question_data = get_questions_opentdb()