class PengirimanBarang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi
        harga = 5000 if volume < 50 or self.berat < 1 else 5000 + (self.berat - 1) * 5000
        return f"Harga: Rp {harga}"

if __name__ == "__main__":
    pengiriman = PengirimanBarang(5, 2, 4, 1)
    print(pengiriman.hitung_harga())