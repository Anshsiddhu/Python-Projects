MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 20,
    },
    "dalgona": {
        "ingredients": {
            "water": 250,
            "milk": 150,
            "coffee": 50,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water_left = resources["water"]
milk_left = resources["milk"]
coffee_powder = resources["coffee"]
ei = MENU["espresso"]
ci = MENU["cappuccino"]
di = MENU["dalgona"]


def money():
    total = (int(input("No. of Rs 10 coins :"))) * 10
    total += (int(input("No. of Rs 5 coins :"))) * 5
    total += (int(input("No. of Rs 2 coins :"))) * 2
    total += (int(input("No. of Rs 1 coins :"))) * 1
    if input1 == "dalgona":
        if di["cost"] > total:
            print("Sorry!")
        else:
            result = total - di["cost"]
            if result == 0:
                print(" ")
            else:
                print(f"Your change = {result}")
    elif input1 == "espresso":
        if ei["cost"] > total:
            print("Sorry!")
        else:
            result = total - ei["cost"]
            if result == 0:
                print(" ")
            else:
                print(f"Your change = {result}")
    else:
        if ci["cost"] > total:
            print("Sorry!")
        else:
            result = total - ci["cost"]
            if result == 0:
                print(" ")
            else:
                print(f"Your change = {result}")


def resources_formatting(order_ingredinents):
    for item in order_ingredinents:
        resources[item] -= order_ingredinents[item]
    print("Hi,Customer")

machine = True
while machine:
    input1 = input("Do you want ?(Type 'espresso','dalgona','cancel' or 'cappuccino'):")


    def resources_checker(order):
        for item in resources:
            if order[item] > resources[item]:
                print(f"​Sorry there is not enough {item}.")
                return False
        return True


    if input1 == "cancel":
        machine = False
    elif input1 == "report":
        if profit == 0:
            print(f'''water level = {water_left}
coffee powder left = {coffee_powder}
milk = {milk_left}''')
        else:
            print(profit)
            print(f'''water level = {water_left}
coffee powder left = {coffee_powder}
milk = {milk_left}''')
    else:
        money()
        if input1 == "off":
            machine = False
        elif input1 == "espresso":
            resources_checker(ei["ingredients"])
            if resources_checker(ei["ingredients"]):
                resources_formatting(ei["ingredients"])
                print("Enjoy! Your coffee")
            else:
                print("Sorry")
        elif input1 == "dalgona":
            resources_checker(di["ingredients"])
            if not resources_checker(di["ingredients"]):
                resources_formatting(di["ingredients"])
                print("Sorry")
            else:
                print("Enjoy! Your coffee")
        elif input1 == "cappuccino":
            resources_checker(ci["ingredients"])
            if resources_checker(ci["ingredients"]):
                resources_formatting(ci["ingredients"])
                print("Enjoy! Your coffee")
            else:
                print("Sorry")
        else:
            print("Please!Enter some value ")
