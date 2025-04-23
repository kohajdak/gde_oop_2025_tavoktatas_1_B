from menu import menu_print, get_valid_menu_input
from utility import clear_screen


def jaratok_listazasa(legi_tarsasag):
    clear_screen()
    print("Elérhető járatok:")
    print("=" * 30 + "")
    for jarat in legi_tarsasag.jaratok:
        print(jarat.jarat_info())
        print("-" * 30)
    input("\nA folytatáshoz nyomjon meg egy billentyűt...")


def foglalas(jegy_foglalas, legi_tarsasag):
    print("Elérhető járatok azonosítói:")
    for jarat in legi_tarsasag.jaratok:
        print(f"- {jarat.jaratszam}")

    jaratszam = input("\nAdja meg a járatszámot: ")
    utas_nev = input("Adja meg az utas nevét: ")
    jarat = next((j for j in legi_tarsasag.jaratok if j.jaratszam == jaratszam), None)
    if jarat:
        print(jegy_foglalas.jegy_foglalasa(jarat, utas_nev))
    else:
        print("Hiba: Nem található ilyen járatszám!")
    input("\nA folytatáshoz nyomjon meg egy billentyűt...")


def foglalasok_kezelese(jegy_foglalas):
    while True:
        clear_screen()
        menu_print("manage")
        menu_selected = get_valid_menu_input([0, 1, 2], "\nVálasszon ki egy menüpontot!\n> ", "manage")

        if menu_selected == 1:
            clear_screen()
            print("Aktív foglalások:")
            print(jegy_foglalas.foglalasok_listazasa())
            input("\nA folytatáshoz nyomjon meg egy billentyűt...")
        elif menu_selected == 2:
            try:
                foglalas_id = int(input("Adja meg a lemondani kívánt foglalás ID-jét: "))
                utas_nev = input("Adja meg az utas nevét: ")
                print(jegy_foglalas.foglalas_lemondasa(foglalas_id, utas_nev))
            except ValueError:
                print("Hiba: Az ID csak szám lehet!")
            input("\nA folytatáshoz nyomjon meg egy billentyűt...")
        elif menu_selected == 0:
            break
