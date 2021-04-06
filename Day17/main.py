###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 17 project - Christopher Hagan
#
###################################

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    question_bank.append(Question(question_text=question['question'], question_answer=question['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print('***\nCongratulations, you\'ve completed the quiz')
print('Your final score was: {}/{}\n***'.format(quiz.score, len(question_bank)))
