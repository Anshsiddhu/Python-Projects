StockAA = 5
StockAAA = 10
then = True
while then:
    name = input("What's your name?")
    if name == "report":
        print(f'''HI , Ansh
    Stock of AA cell left = {StockAA}
    Stock of AAA cell left = {StockAAA}''')
    elif name == "end":
        then = False
    else:
        ph = int(input("Please provide your phone number?"))
        num = len(f"{ph}")
        if num < 10 or num > 10:
            print("invalid phone number")
        else:
            print("Thank you for providing information")
        cell = input("What kind of cell you want?(AA or AAA)")
        quantity = input("How many cells you need ?")
        num = quantity


        def stockchecker():
            if cell == "AA":
                if StockAA == 0 :
                    return False
                else:
                    return True
            else:
                if StockAAA == 0 :
                    return False
                else:
                    return True


        def printer():
            stockchecker()
            if stockchecker():
                return print("Here is your Cells!")
            else:
                return print("Sorry no Stock left")


        stockchecker()
        if stockchecker():
            if cell == "AA":
                if num == 0 or int(num) > StockAA :
                    print("Sorry , we don't have that much stock")
                else:
                    StockAA -= int(num)
                    printer()
            else:
                if num == 0 or int(num) > StockAAA:
                    print("Sorry , we don't have that much stock")
                else:
                    StockAAA -= int(num)
                    printer()
        else:
            printer()
