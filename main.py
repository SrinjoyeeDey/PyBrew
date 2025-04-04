import random
MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,

    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,

    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,

    }
}

profit=0
resources={
            "water":500,
            "coffee":200,
            "milk":300,
}

funny_names=["Mocha","Brew","Bean","SassySip","Boss","Wizard","Lava"]

def is_resources_sufficient(ingredientsOfOrder):
    is_enough=True
    for item in ingredientsOfOrder:
        if ingredientsOfOrder[item]>=resources[item]:

            print(f"Sorry there is not enough {item}.")
            is_enough=False
    return is_enough

def money():
    print("Please insert your coins ")
    total=int(input("How many Quarters?: "))*0.25
    total+=int(input("How many Dimes?: "))*0.1
    total+=int(input("How many Nickels?: "))*0.05
    total+=int(input("How many Pennies?: "))*0.01
    return total

def is_transactionSuccessful(money_received,drinkCost):
    if money_received>=drinkCost:
        change=round(money_received-drinkCost,2)
        print(f"Here is the ${change} in change")
        global profit
        profit+=drinkCost
        return True
    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False

def makeCoffee(drinkName,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Miss/Mr. {code_name}. Here is your {drinkName} ☕. Enjoy!!")


is_on=True

print("Welcome to Srinjoyee's BrewHub 😄")
name=input("Enter your name: ")
birthday=input("Enter your birth year: ")

randomName=random.choice(funny_names)

code_name=f"{randomName} {name[:3]}{birthday}"

while is_on:
    
    user_choiceOfDrink=input("What would you like to have? (espresso/Latte/cappuccino/report): ").lower()

    if user_choiceOfDrink=="off":
        is_on=False
    elif user_choiceOfDrink=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
        
    else:
        drink=MENU[user_choiceOfDrink]
        if is_resources_sufficient(drink['ingredients']):
            payment=money()
            if is_transactionSuccessful(payment,drink['cost']):
                makeCoffee(user_choiceOfDrink,drink["ingredients"])


