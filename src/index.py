from varasto import Varasto

class Main:
    '''Täältä käytetään varastoa tavalla jota en
    itse ikinä noudattaisi, mutta oli kiire saada pylint hiljaiseksi'''

    def __init__(self):
        '''main käynnistää varaston toiminnan'''
        self.mehua = Varasto(100.0)
        self.olutta = Varasto(100.0, 20.2)
        self.luonnin_jalkeen()

    def luonnin_jalkeen(self):
        '''juuh'''
        print("Luonnin jälkeen:")
        print(f"Mehuvarasto: {self.mehua}")
        print(f"Olutvarasto: {self.olutta}")
        self.olut_getterit()

    def olut_getterit(self):
        '''elikkäs'''
        print("Olut getterit:")
        print(f"saldo = {self.olutta.saldo}")
        print(f"tilavuus = {self.olutta.tilavuus}")
        print(f"paljonko_mahtuu = {self.olutta.paljonko_mahtuu()}")


    def mehu_setterit(self):
        '''aivan hirveetä'''
        print("Mehu setterit:")
        print("Lisätään 50.7")
        self.mehua.lisaa_varastoon(50.7)
        print(f"Mehuvarasto: {self.mehua}")
        print("Otetaan 3.14")
        self.mehua.ota_varastosta(3.14)
        print(f"Mehuvarasto: {self.mehua}")
        self.virhetilanteita()

    def virhetilanteita(self):
        '''Vielä yritän kommentoida'''
        print("Virhetilanteita:")
        print("Varasto(-100.0);")
        huono = Varasto(-100.0)
        print(huono)

        print("Varasto(100.0, -50.7)")
        huono = Varasto(100.0, -50.7)
        print(huono)
        self.olutta_lisaa_varastoon()

    def olutta_lisaa_varastoon(self):
        '''Kyllä tämä vaan on kommentti'''
        print(f"Olutvarasto: {self.olutta}")
        print("olutta.lisaa_varastoon(1000.0)")
        self.olutta.lisaa_varastoon(1000.0)
        print(f"Olutvarasto: {self.olutta}")
        self.lisaa_mehua_varastoon()

    def lisaa_mehua_varastoon(self):
        '''aaaa'''
        print(f"Mehuvarasto: {self.mehua}")
        print("mehua.lisaa_varastoon(-666.0)")
        self.mehua.lisaa_varastoon(-666.0)
        print(f"Mehuvarasto: {self.mehua}")
        self.ota_olutta()

    def ota_olutta(self):
        print(f"Olutvarasto: {self.olutta}")
        print("olutta.ota_varastosta(1000.0)")
        saatiin = self.olutta.ota_varastosta(1000.0)
        print(f"saatiin {saatiin}")
        print(f"Olutvarasto: {self.olutta}")
        self.ota_mehua()

    def ota_mehua(self):
        print(f"Mehuvarasto: {self.mehua}")
        print("mehua.otaVarastosta(-32.9)")
        saatiin = self.mehua.ota_varastosta(-32.9)
        print(f"saatiin {saatiin}")
        print(f"Mehuvarasto: {self.mehua}")


if __name__ == "__main__":
    main = Main()
