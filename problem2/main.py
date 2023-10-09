import math

class BangunRuang:
    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_volume(self):
        volume = self.sisi ** 3
        return f"Kubus: {volume}"

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return f"Balok: {volume}"

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def hitung_volume(self):
        volume = math.pi * self.jari_jari ** 2 * self.tinggi
        return f"Tabung: {volume:.2f}"

if __name__ == "__main__":
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)
    print ('Volume')
    print(kubus.hitung_volume())
    print(balok.hitung_volume())
    print(tabung.hitung_volume())