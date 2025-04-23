class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []

    def jegy_foglalasa(self, jarat, utas_nev):
        foglalas_id = len(self.foglalasok) + 1
        self.foglalasok.append({"id": foglalas_id, "utas": utas_nev, "jarat": jarat})
        return f"\nFoglalás sikeres!\n\nFoglalás ID: {foglalas_id}\n{jarat.jarat_info()}" f"\nUtas: {utas_nev}"

    def foglalas_lemondasa(self, foglalas_id, utas_nev):
        for foglalas in self.foglalasok:
            if foglalas["id"] == foglalas_id and foglalas["utas"] == utas_nev:
                self.foglalasok.remove(foglalas)
                return f"\nFoglalás lemondva!\n\nFoglalás ID: {foglalas_id}\n{foglalas['jarat'].jarat_info()}\nUtas: {utas_nev}"
        return "Hiba: Nincs ilyen foglalás az adott ID-val és névvel!"

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincsenek aktív foglalások."
        else:
            output = "=" * 30 + "\n"
            for foglalas in self.foglalasok:
                output += f"Foglalás ID: {foglalas['id']}\n"
                output += f"Járat: {foglalas['jarat'].jarat_info()}\n"
                output += f"Utas: {foglalas['utas']}\n"
                output += "-" * 30 + "\n"
            return output
