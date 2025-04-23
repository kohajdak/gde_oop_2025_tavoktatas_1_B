class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar, indulas, erkezes, idotartam):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.indulas = indulas
        self.erkezes = erkezes
        self.idotartam = idotartam

    def jarat_info(self):
        pass


class BelfoldiJarat(Jarat):
    def jarat_info(self):
        return (
            f"Belföldi járat - Járatszám: {self.jaratszam}\n"
            f"Célállomás: {self.celallomas}\n"
            f"Jegyár: {self.jegyar} HUF\n"
            f"Indulás: {self.indulas} óra\n"
            f"Érkezés: {self.erkezes} óra\n"
            f"Időtartam: {self.idotartam} óra"
        )


class NemzetkoziJarat(Jarat):
    def jarat_info(self):
        return (
            f"Nemzetközi járat - Járatszám: {self.jaratszam}\n"
            f"Célállomás: {self.celallomas}\n"
            f"Jegyár: {self.jegyar} HUF\n"
            f"Indulás: {self.indulas} óra\n"
            f"Érkezés: {self.erkezes} óra\n"
            f"Időtartam: {self.idotartam} óra"
        )


class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)
