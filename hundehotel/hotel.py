from typing import List

class Hund:
    """Description of the Hund Class

    This Class defines the Name, age and its allergies.
    """
    def __init__(self, name: str, alter: int, allergie_liste : List[str] ):
        """Initialized the dog-object.

        The parameters are conveyed to their corresponding self-equivalents.

        Parameters
        ----------
        name : str
            `Name` is the `name` of the dog.

        alter : int
            'alter' is the age of the dog.

        allergie_liste : list
            'allergie_liste' lists the allergies of the dog.
        """
        self.name = name
        self.alter = alter
        self.allergie_liste = allergie_liste

    def __str__(self):
        """Description of the dog.

        This function returns a string, which describes the dog.

        Returns
        -------
        str
            Describes the dog's name, age and allegies

        """
        return f'Hund(Name:{self.name}, Alter:{self.alter}, Allergien{self.allergie_liste}'

    def ist_allergisch(self, allergen : str) -> bool:
        """Checks the allergies of a dog

        This function checks whether the committed allergen is in the dogs allergy list.

        Parameters
        ----------
        allergen : str
            Is the allergen we want to look up in the allergy list of the dog.

        Returns
        -------
        bool
            Returns True or False depending on whether the allergy is in the dog's allergy or not.
        """
        return allergen in self.allergie_liste


# Schneller Textcode den ich nur hier zum rumprobieren verwende
if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 4, ["semmel", "extrawurst"])
    print(rex)
    print(rex.ist_allergisch("semmel"))
    print(rex.ist_allergisch("brot"))


