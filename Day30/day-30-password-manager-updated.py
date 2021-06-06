###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 30 project - Christopher Hagan
#
###################################

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for n in range(0, random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for n in range(0, random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for n in range(0, random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Clear password entry in case the use clicks generate password multiple times
    password_entry.delete(0, END)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'user': username,
            'password': password,
        }
    }

    if not website or not username or not password:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty')
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website, message='These are the details entered: \nUser: {}\nPassword: {}'.format(username, password))

    if is_ok:
        try:
            with open(file='data.json', mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print('File did not exist prior to execution')
            data = new_data
        else:            
            data.update(new_data)
        finally:
            with open(file='data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)
            
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def search_file():
    search_website = website_entry.get()
    try:
        with open(file='data.json', mode='r') as data_file:
                data = json.load(data_file)
        messagebox.showinfo(title=search_website, message='Username : {}\nPassword: {}'.format(data[search_website]['user'], data[search_website]['password']))
    except FileNotFoundError:
        messagebox.showerror(message='The data file does not yet exist')
    except KeyError:
        messagebox.showwarning(message='There is no entry for the website {}'.format(search_website))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = Entry(width=14)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_search = Button(text='Search', command=search_file, width=14)
website_search.grid(column=2, row=1)

username_label = Label(text='Email/username:')
username_label.grid(column=0, row=2)
username_entry = Entry(width=28)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'c.hagan1985@icloud.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(width=14)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text='Generate Password', command=password_generator, width=14)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=28, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

window.mainloop()
