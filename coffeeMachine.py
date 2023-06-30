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
    "water": 800,
    "milk": 200,
    "coffee": 100,
}

# TODO 2. After the user choose what to drink. Check if resourses are available or not. If yes then continue else print that there are no sufficient resourses

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough items.")
            return False
    return True

# # TODO 3. Process Coins. As the machine is coin orieneted.It will acccept coins to complete the process and serve the coffee. b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def take_coints():
    total = float(input("How many quaters?: ")) * 0.25
    total += float(input("How many dimes?: "))*0.10
    total += float(input("How many nickles?: ")) * 0.05
    total += float(input("How many pennies?:)")) * 0.01
    return total

# # TODO 4. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

def transaction_success(money_received , coffee_cost):
    if money_received < coffee_cost:
        print("Not enough money. Money Refunded")
        return False
    elif money_received >= coffee_cost:
        global profit
        profit += money_received        
        print(f"Change returned:- {round(money_received - coffee_cost , 2)}")
        return True
    
#.TODO 5.  Make Coffee.a. If the transaction is successful and there are enough resources to make the drink the usr selected, then the ingredients to make the drink should be deducted from the coffee machine resources


def make_coffee(choice , order_ingri):
    for items in order_ingri:
        resources[items] -= order_ingri[items]
    print("Here's your coffee. ENJOY ;)")  



    
is_on = True

while is_on:
    Choice = input("“What would you like? (espresso/latte/cappuccino):")

    if Choice == 'off':
        is_on = False

    elif Choice == 'report':
        print(resources)
    
    else:
        drink = MENU[Choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = take_coints()
            if transaction_success(payment , drink["cost"] ):
                make_coffee(Choice , drink["ingredients"])
    

  
