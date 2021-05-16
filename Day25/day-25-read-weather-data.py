###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 25 exercises - Christopher Hagan
#
###################################

# import csv

# weather_data_csv = 'weather_data.csv'
# weather_data = []

# with open ('./weather_data.csv'.format(weather_data_csv)) as weather_data_file:
#     reader = csv.DictReader(weather_data_file)
#     for line in reader:
#          weather_data.append(line)

# print(weather_data)

# temperatures = []
# for day in weather_data:
#     temperatures.append(int(day['temp']))

# print(temperatures)

import pandas

weather_data_csv = 'weather_data.csv'

data = pandas.read_csv(weather_data_csv)
temperatures = data['temp'].to_list()

total_temp = 0
for day_temp in temperatures:
    total_temp += day_temp

average_temp = total_temp/ len(temperatures)
print('Average temperature for the week is {}'.format(round(average_temp, 2)))

pandas_mean = data['temp'].mean()
print('\nAnd the pandas mean would be {}'.format(pandas_mean))

pandas_max = data['temp'].max()
print('\nThe pandas max is {}'.format(pandas_max))

print('\nThe day with the highest temperature is:\n {}'.format(data[data.temp == data.temp.max()]))

monday = data[data.day == 'Monday']
print('\nMonday\'s temperature in Fahrenheit {}F'.format(int(monday['temp']) * (9 / 5) + 32))

# Creating a dataframe
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
student_data = pandas.DataFrame(data_dict)
student_data.to_csv('new_data.csv')
