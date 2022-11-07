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
    
    def test_tilavuus_ali_nolla(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
    
    def test_saldo_nolla_jos_annettu(self):
        self.varasto = Varasto(10, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_saldo_nolla_jos_annettu_negatiivinen(self):
        self.varasto = Varasto(10, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisatty_maara_pienempi_kuin_nolla(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_lisatty_maara_ei_mahdu(self):
        self.varasto.lisaa_varastoon(555)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_varastosta_ei_oteta_jos_saldo_nolla(self):
        annettu = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(annettu, 0)
    
    def test_varastosta_ei_oteta_negatiivista_summaa(self):
        self.varasto.lisaa_varastoon(5)
        annettu = self.varasto.ota_varastosta(-7)
        self.assertAlmostEqual(annettu, 0)
    
    def test_varastosta_ei_oteta_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        annettu = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(annettu, 5)
    
    def test_varaston_saa_otettua_tyhjaksi(self):
        self.varasto.lisaa_varastoon(5)
        annettu = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_merkkijonotulostus_toimii(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10.0")