class gaji:
    def __init__(self,idk,nama,jamkerja):
        self.idk = idk
        self.nama = nama
        self.jamkerja = jamkerja

    def gajipokok(self):
        if self.jamkerja == 40:
            return 40 * 30000
        else:
            return self.jamkerja * 30000

    def lembur(self):
        if self.jamkerja > 40:
            return (self.jamkerja - 40) * 45000
        else:
            return 0

    def gajikotor(self):
        return self.gajipokok() + self.lembur()

    def pajak(self):
        if self.gajikotor() >=  1500000 :
            return self.gajikotor() * 5 // 10
        else:
            return 0

    def gajibersih(self):
        return self.gajikotor() - self.pajak()

    def slip(self):
        print("==== Slip Gaji ====")
        print("Id Karyawan      :", self.idk)
        print("Nama             :", self.nama)
        print("Jam Kerja        :", self.jamkerja)
        print("Gaji Pokok       :", self.gajipokok())
        print("upah Lembur      :", self.lembur())
        print("Gaji Kotor       :", self.gajikotor())
        print("Pajak            :", self.pajak())
        print("Gaji Bersih      :", self.gajibersih())


print("=== SISTEM PENGGAJIAN HONORER ===")

idk = input("id karyawan    :")
nama = input("Nama          :")
jamkerja = int(input("Jam Kerja         :"))

if jamkerja >= 1 and jamkerja <=80:
    karyawan = gaji(idk,nama,jamkerja)
    karyawan.slip()
else:
    print("Jam kerja harus 1 - 80 jam")