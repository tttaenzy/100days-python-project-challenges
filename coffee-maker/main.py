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
}

profit = 0
new_report = {
    'Water': '',
    'Milk': '',
    'Coffee': '',
    'Money': ''
}


# function to check if there is enough ingredient to make a drink
def is_resource_sufficient(order_ingredients):
    """return true if the order ingredient is sufficient in resources. if not,
    return statement saying there is no enough particular item."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is no enough {item}.")
            is_enough = False
    return is_enough


# function is to deduct the ingredients from the resources when the coffee is made successfully
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")


# function of userChoice coffee
def coffee(mycoffee):
    expresso_cost = MENU['espresso']['cost']
    latte_cost = MENU['latte']['cost']
    cappuccino_cost = MENU['cappuccino']['cost']

    drink = MENU[user_choice]
    if is_resource_sufficient(drink["ingredients"]):
        print("please insert coins.\n")
        quater = int(input("how many quaters:? "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("how many nickle?: "))
        penny = int(input("how many penny?: "))
        total_cost = quater * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01
        global profit
        if mycoffee == 'espresso':
            change = round(total_cost - expresso_cost, 2)
            if change < 0:
                print(f"You need more money to buy espresso coffee. espresso is {expresso_cost}")
            else:
                profit += expresso_cost
                print(f"Here is ${change} in change\n")
                make_coffee(mycoffee,drink['ingredients'])
        elif mycoffee == 'cappuccino':
            change = round(total_cost - cappuccino_cost, 2)
            if change < 0:
                print(f"You need more money to buy cappuccino coffee. cappuccino is {cappuccino_cost}")
            else:
                profit += cappuccino_cost
                print(f"Here is ${change} in change\n")
                make_coffee(mycoffee,drink['ingredients'])
        elif mycoffee == 'latte':
            change = round(total_cost - latte_cost, 2)
            if change < 0:
                print(f"You need more money to buy latte coffee. latte is {latte_cost}")
            else:
                profit += latte_cost
                print(f"Here is ${change} in change\n")
                make_coffee(mycoffee, drink['ingredients'])


is_on = True
# start here first
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print(f"water: {resources['water']}ml"),
        print(f"milk: {resources['milk']}ml"),
        print(f"coffee: {resources['coffee']}ml"),
        print(f"Money:${profit}")
    elif user_choice == 'espresso':
        coffee('espresso')
    elif user_choice == 'latte':
        coffee('latte')
    elif user_choice == 'cappuccino':
        coffee('cappuccino')
