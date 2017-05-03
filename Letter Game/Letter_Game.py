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

#Pick a random word
while True:
  start = input("Hit Enter/Return to play the game and 'Q' to exit: ")
  if start.lower() == 'q':
    break
  
  #Picking a random word from the list
  
  secret_word = random.choice(words)
  bad_guesses = []
  good_guesses = []
  
  while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
    #drawing the spaces
    for letter in secret_word:
      if letter in good_guesses:
        print(letter, end = '')
      else:
        print('_', end = '')
        
    print('')
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')
      
    #Taking a guess
    guess = input("Guess a letter: ").lower()
      
    if len(guess) != 1:
      print("Hey, you can only guess a single letter")
      continue
    elif guess in good_guesses or guess in bad_guesses:
      print("Well, you already guessed this letter")
      continue
    elif not guess.isalpha():
      print("Well, you can only guess letters!")
      continue
        
    if guess in secret_word:
      good_guesses.append(guess)
      if len(good_guesses) == len(list(secret_word)):
        print("Hey, you won! The word was {}".format(secret_word))
        break
    else:
      bad_guesses.append(guess)
          
  else:
    print("Nice try, but you didn't win! The word is {}".format(secret_word))
