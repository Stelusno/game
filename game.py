#All Tools 
tools = [
    {
    'name': "Teeth",
    'pay': 1,
    'cost': 0
     },
    {
    'name': "Rusty Scissors",
    'pay': 5,
    'cost': 5
     },
    {
     'name':"Old Push Mower",
     'pay': 50,
     'cost': 25
     },
    {
     'name':"Battery Powered Lawnmower",
     'pay': 100,
     'cost': 50
     },
    {
     'name':"Starving Students",
     'pay': 250,
     'cost': 500
     }
]

#Let player know game has begun
print("Begin Game")

#Default to first/only tool available and show current money
current_tool = tools.pop(0)
current_money = 0

while True: 
#Print current tool being used 
  print(f"Current Tool: {current_tool['name']} / Current Money: {current_money}")


#Input option on whether to Cut Grass or Buy Tool
  user_choice = input("Enter Option: 'Cut Grass' or 'Buy Tool':")

#Conditionals for options that are chosen
  if user_choice == "Cut Grass" and current_tool['name'] == "Teeth":
    current_money += 1
  elif user_choice == "Buy Tool" and current_tool['name'] == "Teeth" and current_money < 5:
    print("Not Enough Money!")
  # elif user_choice == "Cut Grass" and current_tool['name'] == "Teeth":
  #   current_money += 1

#Quit game 
  if user_choice.lower() == "quit":
    print("Exting the game. Goodbye!")
    break 
  
  print(f"The user entered {user_choice}. Current Money:           {current_money}")
  
