###################################
#
# 100 Days of code bootcamp 2022
# (Udemy course by Angela Yu)
# 
# Day 45 exercise - Christopher Hagan
#
###################################

from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')
all_films = soup.find_all(name='h3', class_='title')

films_list = []
for film in reversed(all_films):
    films_list.append(film.get_text())

with open('movies.txt', 'w') as file:
    for film in films_list:
        file.write('{}\n'.format(film))
