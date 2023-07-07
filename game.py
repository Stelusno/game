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
  user_choice = input("Enter Option: 'Cut Grass' or 'Buy Tool':").lower()
#Quit game conditional 
  if user_choice.lower() == "quit":
    print("Exting the game. Goodbye!")
    break 
  print(f"You entered {user_choice}.")
  if user_choice.lower() not in ('cut grass', 'buy tool'):
    print("Not A Valid Option")

#Conditionals for options that are chosen
#Cut Grass Conditionals
  if user_choice == "cut grass" and current_tool['name'] == "Teeth":
    current_money += 1
  elif user_choice == "cut grass" and current_tool['name'] == "Rusty Scissors":
    current_money += 5
  elif user_choice == "cut grass" and current_tool['name'] == "Old Push Mower":
    current_money += 50
  elif user_choice == "cut grass" and current_tool['name'] == "Battery Powered Lawnmower":
    current_money += 100
  elif user_choice == "cut grass" and current_tool['name'] == "Starving Students":
    current_money += 250
#Buy Tool Conditionals
  elif user_choice == "buy tool" and current_tool['name'] == "Teeth" and current_money < 5:
    print("Not Enough Money! Keep Cutting!")
  elif user_choice == "buy tool" and current_tool['name'] == "Rusty Scissors" and current_money < 25:
    print("Not Enough Money! Keep Cutting!")
  elif user_choice == "buy tool" and current_tool['name'] == "Old Push Mower" and current_money < 250:
    print("Not Enough Money! Keep Cutting!" )
  elif user_choice == "buy tool" and current_tool['name'] == "Battery Powered Lawnmower" and current_money < 500:
    print("Not Enough Money! Keep Cutting!")
#Switch Tool Conditionals
  elif user_choice == "buy tool" and current_tool['name'] == "Teeth" and current_money >= 5:
    current_tool = tools.pop(0)
    current_money -= 5
  elif user_choice == "buy tool" and current_tool['name'] == "Rusty Scissors" and current_money >= 25: 
    current_tool = tools.pop(0)
    current_money -= 25
  elif user_choice == "buy tool" and current_tool['name'] == "Old Push Mower" and current_money >= 250: 
    current_tool = tools.pop(0)
    current_money -= 250
  elif user_choice == "buy tool" and current_tool['name'] == "Battery Powered Lawnmower" and current_money >= 500: 
    current_tool = tools.pop(0)
    current_money -= 500


  

  
  
  
#Win Game Condition
  if current_money >= 1000 and current_tool['name'] == "Starving Students" :
    print("You Win!! Game Over!!")
    break 
    
  