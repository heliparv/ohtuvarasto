import unittest
from varasto import Varasto
'''Täällä on varaston testaamiseen tehty luokka'''

class TestVarasto(unittest.TestCase):
    '''Näillä funktioilla testataan varaston toimintaa'''
    def setUp(self):
        '''Luodaan varasto testejä varten'''
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        '''varaston luomisen tulee onnistua'''
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        '''varastolla on annettu tilavuus'''
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        '''Lisättäessä saldo lisääntyy'''
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        '''Kun lisätään vähenee tila'''
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        '''Tahdotaan oikea määrä takaisin jos varastosta otetaan'''
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        ''''Tilan tulee kasvaa jos varastosta ottaa'''
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_ali_nolla(self):
        '''Tilavuuden ei tule olla alle nolla'''
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_saldo_nolla_jos_annettu(self):
        '''Saldon tulee olla nolla jos nolla annettu'''
        self.varasto = Varasto(10, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_nolla_jos_annettu_negatiivinen(self):
        '''Saldon tulee olla nolla jos annettu negatiivinen'''
        self.varasto = Varasto(10, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisatty_maara_pienempi_kuin_nolla(self):
        '''Varastoon ei tehdä negatiivista lisäystä'''
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisatty_maara_ei_mahdu(self):
        '''Katsotaan ettei varastoa ylitäytetä'''
        self.varasto.lisaa_varastoon(555)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_ei_oteta_jos_saldo_nolla(self):
        '''Jos saldo on nolla ei varastosta oteta'''
        annettu = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(annettu, 0)

    def test_varastosta_ei_oteta_negatiivista_summaa(self):
        ''''Vasrastosta ei saa negatiivista summaa ulos'''
        self.varasto.lisaa_varastoon(5)
        annettu = self.varasto.ota_varastosta(-7)
        self.assertAlmostEqual(annettu, 0)
    
    def test_varastosta_ei_oteta_liikaa(self):
        '''Varastosta ei pidä saada liikaa ulos'''
        self.varasto.lisaa_varastoon(5)
        annettu = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(annettu, 5)

    def test_varaston_saa_otettua_tyhjaksi(self):
        ''''Testaa että varasto tyhjenee'''
        self.varasto.lisaa_varastoon(5)
        annettu = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonotulostus_toimii(self):
        '''testaa merkkijonotulostusta'''
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")