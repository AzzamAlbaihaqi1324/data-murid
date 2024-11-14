class Murid:
    def __init__(self, nama, umur, kelas):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas

    def __str__(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Kelas: {self.kelas}"

class DataMurid:
    def __init__(self):
        self.murid_list = []

    def tambah_murid(self, murid):
        self.murid_list.append(murid)

    def tampilkan_murid(self):
        for murid in self.murid_list:
            print(murid)

def main():
    data_murid = DataMurid()

    while True:
        print("\n1. Tambah Murid")
        print("2. Melihat Semua Murid")
        print("3. Keluar")
        pilihan = input("Pilih pilihan : ")

        if pilihan == '1':
            nama = input("Masukkan nama murid: ")
            umur = input("Masukkan umur murid: ")
            kelas = input("Masukkan kelas murid: ")
            murid_baru = Murid(nama, umur, kelas)
            data_murid.tambah_murid(murid_baru)
            print("Murid sudah ditambahkan.")
        elif pilihan == '2':
            print("\nData Murid:")
            data_murid.tampilkan_murid()
        elif pilihan == '3':
            print("Keluar dari data murid.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
