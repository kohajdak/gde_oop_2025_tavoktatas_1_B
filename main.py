from menu import menu_print, get_valid_menu_input
from jarat import BelfoldiJarat, NemzetkoziJarat, LegiTarsasag
from jegy_foglalas import JegyFoglalas
from kezeles import jaratok_listazasa, foglalas, foglalasok_kezelese
from utility import clear_screen


def main():
    legi_tarsasag = LegiTarsasag("KK-Air Hungary")
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B001", "A - B", 5000, "00:45"))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N001", "C - D", 25000, "01:50"))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N002", "E - F", 45000, "03:45"))

    jegy_foglalas = JegyFoglalas()
    jegy_foglalas.jegy_foglalasa(legi_tarsasag.jaratok[0], "Rácz Gábor")
    jegy_foglalas.jegy_foglalasa(legi_tarsasag.jaratok[1], "Szőke László")
    jegy_foglalas.jegy_foglalasa(legi_tarsasag.jaratok[2], "Szűcs Szabina")
    jegy_foglalas.jegy_foglalasa(legi_tarsasag.jaratok[0], "Pásztor Endre")
    jegy_foglalas.jegy_foglalasa(legi_tarsasag.jaratok[1], "Nagy Adél")
    jegy_foglalas.jegy_foglalasa(legi_tarsasag.jaratok[2], "Bogdán Sándor")

    while True:
        menu_print("main")
        menu_selected = get_valid_menu_input([0, 1, 2, 3], "\nVálasszon ki egy menüpontot!\n> ", "main")

        if menu_selected == 1:
            jaratok_listazasa(legi_tarsasag)
        elif menu_selected == 2:
            foglalas(jegy_foglalas, legi_tarsasag)
        elif menu_selected == 3:
            foglalasok_kezelese(jegy_foglalas)
        elif menu_selected == 0:
            clear_screen()
            print("Az alkalmazás bezárásra került!\n")
            break


if __name__ == "__main__":
    main()
