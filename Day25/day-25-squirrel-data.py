###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 25 exercises - Christopher Hagan
#
###################################

import pandas

squirrel_data = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pandas.read_csv(squirrel_data)

count_squirrel_type = data.groupby('Primary Fur Color')
print(count_squirrel_type.count())

grey_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Colour': ['Grey', 'Black', 'Red'],
    'Count': [grey_squirrels, black_squirrels, red_squirrels]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('squirrel_count.csv')
