def show_help():
  print("Hello, I am your personal Shoping list!")
  print("""
Type 'DONE' to exit and see your list
Type 'SHOW' to see the current items on the list
Type 'HELP' to see this menu again
""")

#Making the list
shoping_list = []

show_help()

#Adding items to list
while True:
  item = input('> ')
  
  #Adding some functionality - HELP
  if item == 'HELP':
    show_help()
    continue    
    
  #Adding the Show Function
  if item == 'SHOW':
    for temp in shoping_list:
      print(temp)
      continue
  
  #checking for compltetion
  if item == 'DONE':
    break
  
  shoping_list.append(item)

#printing the list out
print("Here is your list of items:")

for stuff in shoping_list:
  print(stuff)
