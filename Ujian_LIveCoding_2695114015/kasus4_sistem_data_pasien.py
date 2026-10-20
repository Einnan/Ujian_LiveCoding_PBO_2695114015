class pasien:
    def __init__(self,nama,usia):
        self.nama = nama
        self.usia = usia

    def katusia(self):
        if self.usia < 17:
            return "Anak"
        elif self.usia <= 59:
            return "Dewasa"
        else:
            return "Lansia"

class klinik:
    def __init__(self):
        self.daftarpasien = []

    def tambahpasien(self,pasien):
        self.daftarpasien.append(pasien)

    def laporan(self):
        print("\n=== Daftar Pasien Hari Ini ===")

        anak = 0 
        dewasa = 0
        lansia = 0
        total_usia = 0

        for i, pasien in enumerate(self.daftarpasien, start=1):
            print(i, "Nama Pasien  :",pasien.nama)
            print("Usia         :",pasien.usia,"Tahun")
            print("Kategori     :",pasien.katusia())
            print()

            total_usia += pasien.usia

            if pasien.katusia() == "Anak":
                anak += 1

            elif pasien.katusia() == "Dewasa":
                dewasa += 1

            else:
                lansia += 1

        total_pasien = len(self.daftarpasien)
        rata2 = total_usia / total_pasien

        print("=== REKAPITULASI KLINIK ===")
        print("Total Pasien     :",total_pasien)
        print("Rata Rata Usia   :",rata2)
        print("Kategori Anak    :",anak)
        print("Kategori Dewasa  :",dewasa)
        print("Kategori Lansia  :",lansia)
        print("==================================")

klinik = klinik()

print("=== DATA PASIEN KLINIK PRATAMA ===")

while True:
    try:
        jumlah = int(input("Jumlah Kunjungan Pasien :"))

        if jumlah > 0:
            break
        else:
            print("Jumlah pasien harus lebih dari 0")

    except ValueError:
        print("Masukkan jumlah dengan angka")

for i in range(1, jumlah +1):
    print("\nPasien ke-",i)

    nama = input("Nama pasien   :")

    while True:
        try:
            usia = int(input("Usia      :"))

            if 0 <= usia <=120:
                break
            else:
                print("")

        except ValueError:
            print("")

    Pasien = pasien(nama, usia)
    klinik.tambahpasien(Pasien)

klinik.laporan()