from utility import clear_screen


MAIN_MENU = [
    [1, "Járatok listázása"],
    [2, "Jegy foglalása"],
    [3, "Foglalások kezelése"],
    [0, "Kilépés"],
]

MANAGE_MENU = [
    [1, "Foglalások listázása"],
    [2, "Foglalás lemondása"],
    [0, "Vissza"],
]


def menu_print(menu_type):
    clear_screen()

    print("Üdvözöljük a === KK-Air Hungary === társaságunknál!")

    print()

    if menu_type == "main":
        menu_type = MAIN_MENU

    elif menu_type == "manage":
        menu_type = MANAGE_MENU

    for menu_item in menu_type:
        if menu_item[0] != 0:
            print(f"{menu_item[0]} - {menu_item[1]}")
        else:
            print(f"\n{menu_item[0]} - {menu_item[1]}")


def get_valid_menu_input(valid_options, prompt, current_menu):
    while True:
        try:
            user_input = int(input(prompt))

            if user_input in valid_options:
                clear_screen()
                return user_input
            else:
                raise ValueError

        except ValueError:
            clear_screen()
            menu_print(current_menu)
            print("\nRossz bevitel! Kérlek, válassz egy érvényes opciót.")
