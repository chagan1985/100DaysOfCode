###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
#
# Day 15 project - Christopher Hagan
#
###################################

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    print('Water: {}ml'.format(resources['water']))
    print('Milk: {}ml'.format(resources['milk']))
    print('Coffee: {}g'.format(resources['coffee']))
    print('Money: ${}'.format(resources['money']))


def check_enough_resources(drink):
    for ingredient in drink['ingredients']:
        if drink['ingredients'][ingredient] > resources[ingredient]:
            print('Sorry there is not enough {}'.format(ingredient))
            return False
    return True


def check_coinage():
    print('Insert coins.')
    quarters_total = int(input('How many quarters?: ')) * 0.25
    dimes_total = int(input('How many dimes?: ')) * 0.1
    nickels_total = int(input('How many nickels?: ')) * 0.05
    pennies_total = int(input('How many pennies?: ')) * 0.01
    total = quarters_total + dimes_total + nickels_total + pennies_total
    return total


def transaction(payment, drink_cost):
    if payment >= drink_cost:
        refund = payment - drink_cost
        if refund:
            print('Here is ${} dollars in change.'.format(round(refund, 2)))
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded')
        return False


def dispense_drink(drink):
    for ingredient in drink['ingredients']:
        print(ingredient)
        resources[ingredient] = resources[ingredient] - drink['ingredients'][ingredient]


valid_operations = {'drinks': ['espresso', 'latte', 'cappuccino'],
                    'secret': ['end', 'report']}
machine_on = True
while machine_on:
    order = ''
    while not order:
        order = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if order not in valid_operations['drinks'] and order.lower() not in valid_operations['secret']:
            order = ''

    if order in valid_operations['drinks']:
        if check_enough_resources(MENU[order]):
            payment = check_coinage()
            money_correct = transaction(payment, MENU[order]['cost'])
            if money_correct:
                resources['money'] += MENU[order]['cost']
                dispense_drink(MENU[order])
                print('Here is your {}. Enjoy!'.format(order))
    elif order == 'report':
        report()
    elif order == 'end':
        machine_on = False
    else:
        print('Unhandled error!')
