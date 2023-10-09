class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def penjumlahan(self):
        return self.angka1 + self.angka2

    def pengurangan(self):
        return self.angka1 - self.angka2

    def perkalian(self):
        return self.angka1 * self.angka2

    def pembagian(self):
        if self.angka2 == 0:
            return "Tidak dapat dibagi dengan nol"
        else:
            return self.angka1 / self.angka2

if __name__ == "__main__":
    kalkulator1 = Kalkulator(3, 4)
    kalkulator2 = Kalkulator(15, 4)
    kalkulator3 = Kalkulator(10, 10)
    kalkulator4 = Kalkulator(12, 3)

    print(f"Penjumlahan: {kalkulator1.penjumlahan()}")
    print(f"Pengurangan: {kalkulator2.pengurangan()}")
    print(f"Perkalian: {kalkulator3.perkalian()}")
    print(f"Pembagian: {kalkulator4.pembagian()}")