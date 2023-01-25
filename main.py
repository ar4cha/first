import os
clear = lambda: os.system('cls')

def main():
    print("INVENTORY MANAGEMENT")
    print("--------------------")
    print()
    print("Available Options:")
    print()
    print("1 - Add Items To Inventory")
    print("2 - View Inventory")
    print()
    while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            addItemToInventory()
            break
  
def addItemToInventory():
  print("ADD ITEMS TO INVENTORY")
  print("----------------------")
  print("wood", "iron", "coal", "wood")
  while True:
    user_item = input("Item Name: ")
    if user_item != '':
      break
  while True:
      item_amount = input("Item Amount: ")
      if item_amount.isdigit():
        break
  addItemsToFile({user_item: int(item_amount)}, clear=False)
  main()




def viewInventory():
  clear()
  print("VIEW INVENTORY")
  print("--------------")
  print()
  invItems = getInvItems()
  print("ITEMS")
  print("-----")
  print()
  for item in invItems:
    print(f"{item}: {invItems[item]}")

  print()
  print("Available Options:")
  print()
  print("1 - Delete Item")
  print()
def addItemsToFile(userItems: dict, clear: bool):
    if clear:
        f = open('userItems.txt', 'w')
        f.close()
        with open('userItems.txt', 'a') as file:
            for item in userItems:
                file.write(f"{item}: {userItems[item]}")
                file.write('\n')
        return
    invItems = getInvItems()
    for item in userItems:
        if item in invItems:
            invItems[item] += userItems[item]
    with open('userItems.txt', 'a') as file:
        for item in invItems:
            file.write(f"{item}: {invItems[item]}")
            file.write('\n')
          
def addItemsToFile(userItems: dict, clear: bool):
  pass

  
main()