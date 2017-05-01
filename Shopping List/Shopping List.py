print("Hello, I am your personal Shoping list!")
print("Press 'DONE' to exit and see your list")

#Making the list
shoping_list = []

#Adding items to list
while True:
  item = input('> ')
  
  #checking for compltetion
  if item == 'DONE':
    break
  
  shoping_list.append(item)

#printing the list out
print("Here is your list of items:")

for stuff in shoping_list:
  print(stuff)
