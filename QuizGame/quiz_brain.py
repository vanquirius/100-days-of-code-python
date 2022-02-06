# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-02-06

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 17 - Quiz Game

class QuizBrain:
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    # Prompt user for input
    raw_user_input = input("Question " + str(self.question_number) + ". " + str(current_question.text))
    # Validate input
    if raw_user_input not in ("True", "False", "true", "false", "T", "F", "t", "f"):
      print("Invalid answer, please answer true/false")
      raw_user_input = input("Question " + str(self.question_number) + ". " + str(current_question.text))
    # Standardize input
    if raw_user_input in ("True", "true", "T", "t"):
      raw_user_input = "True"
    if raw_user_input in ("False", "false", "F", "f"):
      raw_user_input = "False"
    # Check results
    score = self.check_answer(raw_user_input, current_question.answer)
    return score
  
  def check_answer(self, input_answer, input_current_question):
    # Check results
    if input_answer == input_current_question:
      print("Correct! " + input_current_question)
      score = 1
    else:
      print("Sorry, incorrect! The answer was " + input_current_question)
      score = 0
    return score