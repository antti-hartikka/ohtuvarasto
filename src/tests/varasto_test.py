import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_negatiivinen_tilavuus_ja_saldo(self):
        neg_varasto = Varasto(-1, -1)
        self.assertAlmostEqual(neg_varasto.tilavuus, 0)
        self.assertAlmostEqual(neg_varasto.saldo, 0)

    def test_uuden_varaston_ylitaytto(self):
        full_varasto = Varasto(10, 20)
        self.assertAlmostEqual(full_varasto.saldo, full_varasto.tilavuus)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisaaminen(self):
        self.varasto.lisaa_varastoon(1)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 1)

    def test_varaston_ylitaytto(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto(self):
        self.varasto.lisaa_varastoon(10)
        saatu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu, 0)

    def test_ylisuuri_otto(self):
        self.varasto.lisaa_varastoon(10)
        saatu = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(saatu, 10)

    def test_default_str(self):
        self.assertEqual(self.varasto.__str__(), 'saldo = 0, vielä tilaa 10')


