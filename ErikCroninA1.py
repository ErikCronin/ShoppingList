def main():
    print("Shopping List 1.0 - by Erik Cronin")
    menu_choice = input("Menu:\nR - List Required Items\n"
                        "C - List Completed Items\nA - Add New Item\n"
                        "M - Mark an Item as Completed\nQ - Quit\n"
                        "Please choose an option: ")
    menu_choice = menu_choice.upper()
    while menu_choice != "Q":
        if menu_choice == "R":
            print("You chose R")
            menu_choice_func(menu_choice)
        elif menu_choice == "C":
            print("You chose C")
            menu_choice_func(menu_choice)
        elif menu_choice == "A":
            print("You chose A")
            menu_choice_func(menu_choice)
        elif menu_choice == "M":
            print("You chose M")
            menu_choice_func(menu_choice)
    print("exiting shopping list")


def menu_choice_func(menu_choice):
    menu_select = input("Menu:\nR - List Required Items\n"
                        "C - List Completed Items\nA - Add New Item\n"
                        "M - Mark an Item as Completed\nQ - Quit\n"
                        "Please choose an option: ")
    menu_select = menu_select.upper()
    return menu_select

main()
