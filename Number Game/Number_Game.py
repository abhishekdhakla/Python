import random

def game():
  secret_num = random.randint(1,10)
  i=0
  
  while i<5:
    try:
      user_num = int(input("Please guess a number between 1 and 10: "))
      
    except ValueError:
      print("Hey There, That's not a number!")
      
    else:
      if user_num == secret_num:
        print("Bingo! you got it. The secret number was {}".format(secret_num))
        break
      elif user_num < secret_num:
        print("My number is higher than {}".format(user_num))
      elif user_num > secret_num:
        print("My number is less than {}".format(user_num))
    
    i += 1
    
  else:
    check = input("Do you want to play again? Y/n ")
    if check == 'n':
      print("Bye!")
    else:
      game()
      
game()
