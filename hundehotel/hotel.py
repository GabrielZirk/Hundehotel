from typing import List

class Hund:
    def __init__(self, name: str, alter: int, allergie_liste : List[str] ):
        self.name = name
        self.alter = alter
        self.allergie_liste = allergie_liste

    def __str__(self):
        return f'Hund(Name:{self.name}, Alter:{self.alter}, Allergien{self.allergie_liste}'

    def ist_allergisch(self, allergen : str) -> bool:
        return allergen in self.allergie_liste


# Schneller Textcode den ich nur hier zum rumprobieren verwende
if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 4, ["semmel", "extrawurst"])
    print(rex)
    print(rex.ist_allergisch("semmel"))
    print(rex.ist_allergisch("brot"))


