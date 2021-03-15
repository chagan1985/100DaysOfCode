###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 9 exercises - Christopher Hagan
#
###################################

# Exercise 9-1 Grading program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for student in student_scores:
    if student_scores[student] > 90:
        grade = 'Outstanding'
    elif student_scores[student] > 80:
        grade = 'Exceeds Expectations'
    elif student_scores[student] > 70:
        grade = 'Acceptable'
    else:
        grade = 'Fail'

    student_grades[student] = grade

print(student_grades)


# Exercise 9-2 Travel log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, list_of_cities):
    new_country_entry = {}
    new_country_entry['country'] = country
    new_country_entry['visits'] = visits
    new_country_entry['cities'] = list_of_cities
    travel_log.append(new_country_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print('\n\n{}'.format(travel_log))
