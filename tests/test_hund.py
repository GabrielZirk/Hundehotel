import unittest
from hundehotel.hotel import Hund

class HundeTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("Einmal insgesamt aufgerufen zum Initialisieren")
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("Einmal insgesamt aufgerufen am Ende meines Tests")
    #     pass
    #
    def setUp(self) -> None:
        self.hund =  Hund("Kommissar Rex", 4, ["semmel", "extrawurst"])

    # def tearDown(self) -> None:
    #     print("Einmal nach jedem Test")
    #     pass

    def test_allergie_positiv(self):
        # hier teste ich meine Funktionalität
        erg = self.hund.ist_allergisch("semmel")
        #  und dann überprüfe ich die Korrektheit meines Ergebnisses
        self.assertTrue(erg, "Positive Allergie erkannt")


    def test_allergie_negativ(self):
        # hier teste ich meine Funktionalität
        erg = self.hund.ist_allergisch("brot")
        #  und dann überprüfe ich die Korrektheit meines Ergebnisses
        self.assertFalse(erg, "Keine Allergie korrekt erkannt")


if __name__ == '__main__':
    unittest.main()
