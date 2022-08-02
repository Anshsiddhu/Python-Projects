print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "M":
    bill += 20
elif size == "S":
    bill += 15
else:
    bill += 25
if pepperoni == "Y":
    if size == "S":
         bill += 2
    print(f"Bill=Rs{bill}")
else:
    bill +=3
    print(f"Bill=Rs{bill}")
if cheese == "Y":
    bill += 1
    print(f"Your final bill = Rs{bill}")
else:
    print(f"Your final bill = Rs{bill}")


