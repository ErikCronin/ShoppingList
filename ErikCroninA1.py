def main():
    shopping_list = open("items.csv", "r")
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

            list_of_items.append(new_item())
            print(list_of_items)


        # Mark an item as completed
        elif menu_choice == "M":
            ask_question = True
            while ask_question:
                required_items(list_of_items, "r")
                mark_completion = int(input("Enter the number of an item to be marked as completed. "))
                write_list = list_of_writable_items(list_of_items, "r")
                completed_list = list_of_writable_items(list_of_items, "c")
                if mark_completion < len(write_list):
                    print(write_list[mark_completion])
                    write_list[mark_completion] = write_list[mark_completion] + "c"
                    completed_list.append(write_list[mark_completion])
                    write_list.remove(write_list[mark_completion])
                    list_of_items = write_list + completed_list
                    print(list_of_items)
                    ask_question = False
                else:
                    print("Invalid input!")

        menu_choice = menu_choice_func()
    print("exiting shopping list")


def menu_choice_func():
    menu_select = input("Menu:\nR - List Required Items\n"
                        "C - List Completed Items\nA - Add New Item\n"
                        "M - Mark an Item as Completed\nQ - Quit\n"
                        "Please choose an option: ")
    menu_select = menu_select.upper()
    return menu_select


def required_items(shopping_list, status):
    line_number = 0
    for line_str in shopping_list:
        if line_str[-1] == status:
            line_str = line_str.split(",")
            line_str[1] = float(line_str[1])
            print("{:1}. {:20} ${:10.2f} ({:s})".format(line_number, line_str[0], line_str[1], line_str[2]))
            line_number += 1


def marked_func(shopping_list):
    list_of_items = []
    for item in shopping_list:
        item = item.strip("\n")
        list_of_items.append(item)

    return list_of_items


def list_of_writable_items(shopping_list, status):
    write_list = []
    for line_str in shopping_list:
        if line_str[-1] == status:
            write_list.append(line_str)
    return write_list


def new_item():
    item_name = str(input("Name of new item: "))
    item_price = str(input("Price of new item: "))
    item_priority = str(input("Priority of new item: "))
    new_string = "{},{},{},r".format(item_name, item_price, item_priority)

    print(new_string)
    return new_string


main()