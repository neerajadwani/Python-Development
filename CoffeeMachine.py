import numpy as np

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def compare_resource(coffee, resource):
    left = np.max(resources[resource]-MENU[coffee]['ingredients'][resource], 0)
    return left


def check_resource(coffee):
    global resources
    water_left = compare_resource(coffee,'water')
    coffee_left = compare_resource(coffee, 'coffee')
    if coffee != 'espresso':
        milk_left = compare_resource(coffee, 'milk')
    else:
        milk_left = resources['milk']
    if water_left == 0 or coffee_left == 0 or milk_left == 0:
        print('Requested coffee can not be made as resources are low')
        return 0
    else:
        resources['water'] = water_left
        resources['milk'] = milk_left
        resources['coffee'] = coffee_left
        return 1


def report():
    print(f'water:{resources["water"]} \n milk:{resources["milk"]} \n coffee:{resources["coffee"]} \n Money:{profit}$')
    prompt_user()


def reduce_resources(coffee):
    global resources
    resources['water'] = resources['water']-MENU[coffee]['ingredients']['water']
    resources['coffee'] = resources['coffee']-MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources['milk'] = resources['milk']-MENU[coffee]['ingredients']['milk']


def espresso(total_money):
    global profit
    check = check_resource('espresso')
    if check == 0:
        print('please choose a different coffee')
        prompt_user()
    elif check == 1:
        if total_money<MENU['espresso']['cost']:
            print('Money not enough, Money refunded')
            prompt_user()
        else:
            profit += MENU['espresso']['cost']
            reduce_resources('espresso')
            refund = total_money-MENU['espresso']['cost']
            print(f'Here your {np.round(refund,2)}$ in change')
            print('Here is your espresso. Enjoy!!')
            prompt_user()


def latte(total_money):
    global profit
    check=check_resource('latte')
    if check == 0:
        print('please choose a different coffee')
        prompt_user()
    elif check == 1:
        if total_money<MENU['latte']['cost']:
            print('Money not enough, Money refunded')
            prompt_user()
        else:
            profit += MENU['latte']['cost']
            reduce_resources('latte')
            refund = total_money-MENU['latte']['cost']
            print(f'Here your {np.round(refund,2)}$ in change')
            print('Here is your latte. Enjoy!!')
            prompt_user()


def cappuccino(total_money):
    global profit
    check=check_resource('cappuccino')
    if check == 0:
        print('please choose a different coffee')
        prompt_user()
    elif check == 1:
        if total_money<MENU['cappuccino']['cost']:
            print('Money not enough, Money refunded')
            prompt_user()
        else:
            profit+= MENU['cappuccino']['cost']
            reduce_resources('cappuccino')
            refund= total_money-MENU['cappuccino']['cost']
            print(f'Here your {np.round(refund,2)}$ in change')
            print('Here is your cappuccino. Enjoy!!')
            prompt_user()


def prompt_user():
    coffee=0
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == 'report':
        report()
    else:
        if coffee not in ['espresso', 'latte', 'cappuccino']:
            print('Please insert a correct input')
            prompt_user()
        else:
            quarters = int(input("no of quarters="))
            dimes = int(input("no of dimes="))
            nickles = int(input("no of nickles="))
            pennies = int(input("no of pennies="))
            total_money=0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
            if coffee == 'espresso':
                espresso(total_money)
            elif coffee == 'latte':
                latte(total_money)
            elif coffee == 'cappuccino':
                cappuccino(total_money)
            elif coffee == 'off':
                exit()


prompt_user()
