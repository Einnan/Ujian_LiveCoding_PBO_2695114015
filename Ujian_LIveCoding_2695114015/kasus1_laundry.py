class laundry:
    def __init__(self, namapel,layanan,berat):
        self.namapel = namapel
        self.layanan = layanan 
        self.berat = berat

    def subtotal(self):
        if self.layanan == "reguler":
            harga = 8000

        elif self.layanan == "kilat":
            harga = 12000

        return harga * self.berat

    def diskon(self):
        if self.berat > 10:
            return 0.15

        elif self.berat > 5:
            return 0.10

        else:
            diskon = 0

        return self.subtotal() * diskon

    def potongan(self):
        return self.subtotal() * self.diskon()

    def total_bayar(self):
        return self.subtotal() - self.potongan()

    def nota(self):
        print("========== Nota Pembayaran Laundry ==========")
        print("Nama Pelanggan   :",self.namapel)
        print("Layanan          :",self.layanan)
        print("berat            :",self.berat)
        print("Subtotal         :",self.subtotal(), "kg")
        print("Diskon           :",self.diskon() * 100, "%")
        print("Potongan         :",self.potongan())
        print("Total Bayar      :",self.total_bayar())

print("======== Laundry Clean And Fresh ========")
namapel = input("Nama Pelanggan                 :")
layanan = input("Jenis Layanan (Reguler/Kilat)  :".lower())
berat = float(input("Berat Cucian               :"))

pelanggan = laundry(namapel,layanan, berat)

pelanggan.nota()