# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-02-06

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 17 - Quiz Game

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    ENDC = '\033[m'

# Runtime
print(colors.GREEN + "Quiz Game" + colors.ENDC)
print("Please answer true or false.")

# Initialize empty question bank
question_bank = []
# Loop through question data to populate question bank
for i in question_data:
  question = i["question"]
  answer = i["correct_answer"]
  create_question = Question(question, answer)
  question_bank.append(create_question)

total_score = 0
asked_questions = 0
quiz = QuizBrain(question_bank)
while(quiz.still_has_questions() is True):
  total_score += quiz.next_question()
  asked_questions += 1
  print("Total score: " + str(total_score) + "/" + str(asked_questions))
  print("\n")

print(colors.RED + "End of quiz!" + colors.ENDC)
print("Final score: " + str(total_score) + "/" + str(asked_questions))