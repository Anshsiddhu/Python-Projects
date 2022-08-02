import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
result = len(names)
final = int(result) - 1
num = random.randint(0,int(final))
print(names[num] +" " +"is going to pay the bill of today's meal.")