from menu import menu_print, get_valid_menu_input
from utility import clear_screen
from datetime import datetime


def ervenyes_datum():
    while True:
        datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datetime.strptime(datum, "%Y-%m-%d")
            return datum
        except ValueError:
            print("Hiba: Kérjük, a dátumot YYYY-MM-DD formátumban adja meg!")


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

    while True:
        jaratszam = input("\nAdja meg a járatszámot: ")
        jarat = next((j for j in legi_tarsasag.jaratok if j.jaratszam == jaratszam), None)
        if jarat:
            break
        else:
            print("Hiba: Nem található ilyen járatszám!")

    utas_nev = input("Adja meg az utas nevét: ")
    datum = ervenyes_datum()

    print(jegy_foglalas.jegy_foglalasa(jarat, utas_nev, datum))
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
            while True:
                try:
                    foglalas_id = int(input("Adja meg a lemondani kívánt foglalás ID-jét: "))
                    if foglalas_id <= 0:
                        print("Hiba: Az ID csak pozitív egész szám lehet!")
                        continue
                except ValueError:
                    print("Hiba: Az ID csak pozitív egész szám lehet!")
                    continue

                utas_nev = input("Adja meg az utas nevét: ")

                eredmeny = jegy_foglalas.foglalas_lemondasa(foglalas_id, utas_nev)
                print(eredmeny)

                if "Nincs ilyen foglalás" in eredmeny:
                    input("\nA folytatáshoz nyomjon meg egy billentyűt...")
                    break
                else:
                    input("\nA folytatáshoz nyomjon meg egy billentyűt...")
                    break

        elif menu_selected == 0:
            break
