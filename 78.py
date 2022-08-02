import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the GAME......")
reply = input("What you want to choose for scissors type = 0 , for rock type = 1 and for paper type = 2 :")
num = random.randint(0, 2)
result = int(num)
print("You chooses:")
game_images = [scissors, rock, paper]
print(game_images[int(reply)])
print("Computer chose:")
print(game_images[num])
if int(reply) >= 3 or int(reply) < 0:
  print("You typed an invalid number, you lose!")
elif reply == 0 and num == 2:
  print("You won!")
elif num == 2 and reply == 0:
  print("You lose")
elif num == 1 and reply == 2:
  print("You lose")
elif num == 0 and reply == 1:
  print("You lose")
elif num == 1 and reply == 0:
  print("You won")
elif num == 2 and reply == 1:
  print("You won")
elif num == 2 and reply == 1:
  print("You won")
elif num == reply:
  print("It's a Draw")
elif num > int(reply):
  print("You lose")
elif num > int(reply):
  print("You win!")
elif num == reply:
   print("It's a draw")