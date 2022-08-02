logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to Secret Bid program")
name = input("What is your name?\n")
bid = input("What's your bid(in Rs)?\n")
highest_bid = {}
# others = input("Are there any other bidders?(Type 'yes' or 'no'")
highest_bid[name] = bid
def highest_bider(names1,bids2):
    end = False

    while not end:
        others = input("Are there any other bidders?(Type 'yes' or 'no'")
        if others == "yes":
            names5 = input("What is your name?\n")
            bid6 = input("What's your bid(in Rs)?\n")
            highest_bid[names5] = bid6

        else:
            highest_bid[names5] = bid6
            end = True
# if others == "yes":
    #     names5 = input("What is your name?\n")
    #     bid6 = input("What's your bid(in Rs)?\n")
    #     highest_bid[names5] = bid6
    # else:
    #     for names in highest_bid:
    #         highest_bid[name] = bid
highest_bider(name,bid)
key1 = list(highest_bid.keys())
values1 = list(highest_bid.values())
# print(highest_bid)
# print(key1[values1.index(max(values1))])
max_bid = key1[values1.index(max(values1))]
print(f"{max_bid} is the highest bider.")
print("Thank you for coming in Auction")
print("See you later")