###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 16 project - Christopher Hagan
#
###################################

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks_menu = Menu()
drinks_maker = CoffeeMaker()
transaction_handler = MoneyMachine()
on = True

while on:
    user_choice = input('What would you like to drink ({})?: '.format(
            drinks_menu.get_items())).lower()

    if user_choice in ['report', 'off'] or drinks_menu.find_drink(user_choice) :
        if user_choice == 'off':
            # Handle secret keyword 'off'
            on = False
        elif user_choice == 'report':
            # Handle secret keyword 'report'
            drinks_maker.report()
            transaction_handler.report()
        else:
            # Make the appropriate drink
            drink = drinks_menu.find_drink(user_choice)
            if drinks_maker.is_resource_sufficient(drink):
                print('A {} costs ${}...'.format(drink.name, drink.cost))
                if transaction_handler.make_payment(drink.cost):
                    drinks_maker.make_coffee(drink)
