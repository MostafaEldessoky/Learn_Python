# TODO : 1-What would you like? (espresso/latte/cappuccino):
# TODO : 2-choice or off the machine:
# TODO : 3-take money and refuse if it not enough or back the exceed amount:
# TODO : 4-print recept:
# TODO : 5-report for current machine state:
# -----------------------------------------------
# important data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


# ------------------------------------------------------------
# program functions
def ck_fun(x):
    y1 = resources["water"] - MENU[x]["ingredients"]["water"]
    y2 = resources["milk"] - MENU[x]["ingredients"]["milk"]
    y3 = resources["coffee"] - MENU[x]["ingredients"]["coffee"]
    if y1 <= 0 or y2 <= 0 or y2 <= 0:
        return False
    else:
        return True


def money_fun(x, x1, x2, x3, x4):
    global profit
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    y = x1 * quarters + x2 * dimes + x3 * nickles + x4 * pennies
    if y == MENU[x]["cost"]:
        profit += y
        return 0, True
    elif y < MENU[x]["cost"]:
        return y, False
    else:
        profit += MENU[x]["cost"]
        return y - MENU[x]["cost"], True


def action_fun(x, x1, x2, x3, x4):
    global resources
    y1 = ck_fun(x)
    y2, y3 = money_fun(x, x1, x2, x3, x4)
    if y1 and y3 and y2 == 0:
        resources["water"] -= MENU[x]["ingredients"]["water"]
        resources["milk"] -= MENU[x]["ingredients"]["milk"]
        resources["coffee"] -= MENU[x]["ingredients"]["coffee"]
        return 0, True
    elif y1 and y3 and y2 > 0:
        resources["water"] -= MENU[x]["ingredients"]["water"]
        resources["milk"] -= MENU[x]["ingredients"]["milk"]
        resources["coffee"] -= MENU[x]["ingredients"]["coffee"]
        return y2, True
    elif y1 and not y3:
        return y2, False
    elif not y1:
        return 0, False


# ---------------------------------------------------------------------
# actual program
while True:
    while True:
        q = input("Enter off to turn off the coffee machine, Enter report to print report for the current recourses, "
                  "What would you like? (espresso/latte/cappuccino):").lower()
        if q == "off" or q == "report" or q == "espresso" or q == "latte" or q == "cappuccino":
            break
        else:
            print("sorry not valid input")
    if q == "off":
        break
    elif q == "report":
        print(f"milk: {resources['milk']}\nwater: {resources['water']}\ncoffee: {resources['coffee']}")
    else:
        print(
            f"Please enter needed money: {q} {MENU[q]['cost']}")
        e1, e2, e3, e4 = input("How many quarters, dimes, nickles, pennies : ").split()
        a1, a2 = action_fun(q, int(e1), int(e2), int(e3), int(e4))
        if a1 == 0 and a2:
            print(f"Valid inputs, here is your {q} :\nrecept\ntype :{q}\nprice : ${MENU[q]['cost']}")
        elif a1 != 0 and a2:
            print(
                f"Valid inputs, here is your {q} :\nrecept\ntype :{q}\nprice : ${MENU[q]['cost']}\nthe rest : ${a1}")
        elif a1 != 0 and not a2:
            print(
                f"Invalid inputs, please take your money, try again and enter the required amount of money")
        elif a1 == 0 and not a2:
            print(
                f"sorry no resources are available now, current recourses :\nmilk: {resources['milk']}\nwater: {resources['water']}\ncoffee: {resources['coffee']}")
