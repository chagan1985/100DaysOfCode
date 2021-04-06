###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 17 example - Christopher Hagan
#
###################################

class User:

    def __init__(self, user_id, username):
        print('new user being created...')
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id='001', username='Chris')
user_2 = User(user_id='002', username='Jack')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
