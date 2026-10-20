class paketx:
    def __init__(self,resi,pengirim,layanan,berat,perkiraan):
        self.resi = resi
        self.pengirim = pengirim
        self.layanan = layanan
        self.berat = berat
        self.perkiraan = perkiraan

    def ongkos(self):
        if self.layanan == "reguler":
            return 10000 * self.berat

        elif self.layanan == "express":
            return 18000 * self.berat

        else:
            return 0

    def asuransi(self):
        if self.perkiraan >= 1000000:
            return self.perkiraan * 0.01

        else:
            return 0

    def surcharge(self):
        if self.berat > 10:
            return 20000

        else:
            return 0

    def total(self):
        return self.ongkos() + self.asuransi() + self.surcharge()

    def cetakresi(self):
        if self.berat <= 0 or self.layanan not in ["reguler","express"]:
            return print("Permintaan ditolak !!")

        else:
            print("=== Resi Pengiriman ===")
            print("Nomor Resi       :",self.resi)
            print("Nama Pengirim    :",self.pengirim)
            print("Layanan          :",self.layanan)
            print("Berat            :",self.berat)
            print("Tarif Dasar      :",self.ongkos())
            print("Heavy Surcharge  :",self.surcharge())
            print("Biaya Asuransi   :",self.asuransi())
            print("Total Ongkos     :",self.total())
            print("===============================")

resi = input("Nomor Resi    :")
pengirim = input("Nama Pengirim  :")
layanan = input("Jenis Layanan  :").lower()
berat = int(input("Berat Paket  :"))
perkiraan = int(input("Nilai Barang  :"))

paket = paketx(resi,pengirim,layanan,berat,perkiraan)
paket.cetakresi()