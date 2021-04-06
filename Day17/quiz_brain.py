###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 17 project - Christopher Hagan
#
###################################

class QuizBrain:

    def __init__(self, list_of_questions):
        self.question_number = 0
        self.score = 0
        self.question_list = list_of_questions
 
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        valid_guess = False
        while not valid_guess:
            user_guess = input('Q.{}: {} (True/False)?: '.format(
                                                                self.question_number + 1, 
                                                                self.question_list[self.question_number].text,
                                                                )).lower()
            if user_guess in ['true', 'false', 't', 'f']:
                valid_guess = True
        self.check_answer(user_guess, self.question_list[self.question_number].answer)
        self.question_number += 1
        
    def check_answer(self, user_guess, answer):
        if user_guess.startswith(answer[0].lower()):
            print('Congratulations, you got that one right')
            self.score += 1
        else:
            print('Nope, that\'s wrong, the correct answer was {}.'.format(answer))
        print('Your current score is {}/{}\n\n'.format(self.score, self.question_number + 1))
