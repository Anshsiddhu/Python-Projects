
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horse = int(position[0])
ver = int(position[1])
selected_row= map[horse - 1]
selected_row[ver - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")