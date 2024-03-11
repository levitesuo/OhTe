import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_kassapaate_on_luotu_oikein(self):
        self.assertEqual(str(self.paate), "100000, 0, 0")

    def test_kateinen_maukas_onnistuu(self):
        takaisin = self.paate.syo_maukkaasti_kateisella(440)
        self.assertEqual(str(self.paate) +", " + str(takaisin), "100400, 0, 1, 40")

    def test_kateinen_edullinen_onnistuu(self):
        takaisin = self.paate.syo_edullisesti_kateisella(280)
        self.assertEqual(str(self.paate) +", " + str(takaisin), "100240, 1, 0, 40")

    def test_kateinen_maukas_epaonnistuu(self):
        takaisin = self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(str(self.paate) +", " + str(takaisin), "100000, 0, 0, 200")

    def test_kateinen_edullinen_epaonnistuu(self):
        takaisin = self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.paate) +", " + str(takaisin), "100000, 0, 0, 200")

    def test_kortti_edullinen_onnistuu(self):
        onnistunut = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.paate) +", " + str(onnistunut), "100000, 1, 0, True")

    def test_kortti_edullinen_epaonnistuu(self):
        kortti = Maksukortti(10)
        onnistunut = self.paate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.paate) +", " + str(onnistunut), "100000, 0, 0, False")

    def test_kortti_maukas_onnistuu(self):
        onnistunut = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.paate) +", " + str(onnistunut), "100000, 0, 1, True")
        
    def test_kortti_maukas_epaonnistuu(self):
        kortti = Maksukortti(10)
        onnistunut = self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.paate) +", " + str(onnistunut), "100000, 0, 0, False")
    
    def test_kortille_rahan_lataaminen(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(str(self.paate)+", "+str(self.kortti), "101000, 0, 0, Kortilla on rahaa 20.00 euroa")
    
    def test_kortille_negatiivisen_rahan_lataaminen(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(str(self.paate)+", "+str(self.kortti), "100000, 0, 0, Kortilla on rahaa 10.00 euroa")
'''

Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla'''