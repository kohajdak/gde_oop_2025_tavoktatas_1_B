class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def jegy_foglalasa(self, jarat, utas_nev):
        self.foglalasok.append({"utas": utas_nev, "jarat": jarat})
        return f"\nFoglalás sikeres!\n\n{jarat.jarat_info()}" f"\nUtas: {utas_nev}"

    def foglalas_lemondasa(self, utas_nev):
        for foglalas in self.foglalasok:
            if foglalas["utas"] == utas_nev:
                self.foglalasok.remove(foglalas)
                return f"\nFoglalás lemondva!\n\n{foglalas['jarat'].jarat_info()}\nUtas: {utas_nev}"
        return "Nincs ilyen foglalás!"

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincsenek aktív foglalások."
        else:
            output = "=" * 30 + "\n"
            for foglalas in self.foglalasok:
                output += f"Járat: {foglalas['jarat'].jarat_info()}\n"
                output += f"Utas: {foglalas['utas']}\n"
                output += "-" * 30 + "\n"
            return output
