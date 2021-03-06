"""
Erik Cronin
09/09/2016
This program aims to create a shopping list.
Users can show completed or needed items, add their own items and
check off the required items into the completed category.
Github: https://github.com/ErikCronin/ShoppingList
"""


def main():
    shopping_list = open("items.csv", "r+")
    list_of_items = marked_func(shopping_list)
    print("Shopping List 1.0 - by Erik Cronin")
    menu_choice = menu_choice_func()
    while menu_choice != "Q":

        # List Required Items
        if menu_choice == "R":
            required_items(list_of_items, "r")

        # List Completed Items
        elif menu_choice == "C":
            required_items(list_of_items, "c")

        # Add New Items
        elif menu_choice == "A":
            item_name = str(input("Enter the name of the new item: "))
            item_price = str(input("Enter the price of the new item: "))
            item_priority = str(input("Enter the priority of the new item: "))
            new_item_list = item_name + "," + item_price + "," + item_priority + ",r"
            list_of_items.append(new_item_list)
            print(item_name, "has been added to the list")

        # Mark an item as completed
        elif menu_choice == "M":
            ask_question = True
            while ask_question:
                required_items(list_of_items, "r")
                while True:
                    try:
                        mark_completion = int(input("Enter the number of an item to be marked as completed. "))
                        break
                    except ValueError:
                        print("You did not enter a number. Please enter a number.")
                write_list = list_of_writable_items(list_of_items, "r")
                completed_list = list_of_writable_items(list_of_items, "c")
                if mark_completion < len(write_list):
                    print("Item number", mark_completion, "has been marked off")
                    write_list[mark_completion] += "c"
                    completed_list.append(write_list[mark_completion])
                    write_list.remove(write_list[mark_completion])
                    list_of_items = write_list + completed_list
                    ask_question = False
                else:
                    print("Invalid input!")
                    
        # Error Check
        else:
            print("Invalid Input! Please try again.")

        menu_choice = menu_choice_func()
    shopping_list = open("items.csv", "w")
    for item in list_of_items:
        shopping_list.writelines(item + '\n')
    shopping_list.close()
    print("Shopping list has been saved.\nHave a nice day :)")


# Function for choosing menu option
def menu_choice_func():
    menu_select = input("Menu:\nR - List Required Items\n"
                        "C - List Completed Items\nA - Add New Item\n"
                        "M - Mark an Item as Completed\nQ - Quit\n"
                        "Please choose an option: ")
    menu_select = menu_select.upper()
    return menu_select


# Function to show required items (r) or completed items (c)
def required_items(shopping_list, status):
    line_number = 0
    for line_str in shopping_list:
        if line_str[-1] == status:
            line_str = line_str.split(",")
            line_str[1] = float(line_str[1])
            print("{:1}. {:20} ${:10.2f} ({:s})".format(line_number, line_str[0], line_str[1], line_str[2]))
            line_number += 1
    return line_str


# Function to load shopping list into internal memory
def marked_func(shopping_list):
    list_of_items = []
    for item in shopping_list:
        item = item.strip("\n")
        list_of_items.append(item)
    return list_of_items


# Function to add items to completed list
def list_of_writable_items(shopping_list, status):
    write_list = []
    for line_str in shopping_list:
        if line_str[-1] == status:
            write_list.append(line_str)
    return write_list


main()
