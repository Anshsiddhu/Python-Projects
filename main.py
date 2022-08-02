from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
dr = menu.get_items()
on = True
while on:
    n = input(f"What drink you want?{dr}")
    if n == "off":
        on = False
    elif n == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(n)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)