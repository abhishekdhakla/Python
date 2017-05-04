import os
import sys
import random

words = [
  'apple',
  'banana',
  'orange',
  'coconut',
  'strawberry',
  'lime',
  'grapefruit',
  'lemon',
  'kumquat',
  'blueberry',
  'melon'
]

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

    
def draw(bad_guesses, good_guesses, secret_word):
  clear()
  print('Strikes: {}/7'.format(len(bad_guesses)))
  print('')
  
  for letter in bad_guesses:
    print(letter, end = ' ')
    print('')
  
  for letter in secret_word:
    if letter in good_guesses:
      print(letter, end = '')
    else:
      print('_', end = '')
      
  print('')
      
  
def get_guess(good_guesses, bad_guesses):
  while True:
    guess = input("Guess a letter: ").lower()
      
    if len(guess) != 1:
      print("Hey, you can only guess a single letter")
    elif guess in good_guesses or guess in bad_guesses:
      print("Well, you already guessed this letter")
    elif not guess.isalpha():
      print("Well, you can only guess letters!")
    else:
      return guess
    
    
def play(done):
  clear()
  secret_word = random.choice(words)
  bad_guesses = []
  good_guesses = []
  
  while True:
    draw(bad_guesses, good_guesses, secret_word)
    guess = get_guess(good_guesses, bad_guesses)
    
    if guess in list(secret_word):
      good_guesses.append(guess)
      found = True
      for letter in list(secret_word):
        if letter not in good_guesses:
          found = False
      
      if found:
        print("Hey, you won! The word was {}".format(secret_word))
        done = True
        
    else:
      bad_guesses.append(guess)
      if len(bad_guesses) == 7:
        print("Nice try, but you didn't win! The word is {}".format(secret_word))
        done = True
        
    if done:
      play_again = input("Play again? Y/n ").lower()
      if play_again != 'n':
        return play(done = False)
      else:
        sys.exit()
          
def welcome():
  start = input("Press Enter/Return to play the game and 'Q' to exit: ").lower()
  if start == 'q':
    print("Bye!")
    sys.exit()
    
  else:
    return True
  
print("Welcome to Letter Game!")

done = False
  
while True:
  clear()
  welcome()
  play(done) 
  
