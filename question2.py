# 2. The Shopping List Maker

# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.

shopping_list = []

def add_to_list(item_to_add):
    shopping_list.append(item_to_add)

def remove_from_list(item_to_remove):
    shopping_list.remove(item_to_remove)

while True:
    operation_to_perform = input("Add, remove, print shopping list or quit: ").lower()
        
    if(operation_to_perform == "add"):
        add_to_list(input("Item to add to shopping list: ").lower())

    if(operation_to_perform == "remove"):
        remove_from_list(input("Item to remove from shopping list: ").lower())
        
    if(operation_to_perform == "print"):
        for iteration, item in enumerate(shopping_list):
            print(f'Item no. {iteration+1}: {item}')

    if(operation_to_perform == "quit"):
        print("Exiting shopping list program!")
        break