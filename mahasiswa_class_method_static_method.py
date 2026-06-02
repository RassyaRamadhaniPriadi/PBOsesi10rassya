# Nama  : Rassya Ramadhani Priadi
# NIM   : 20230040142
# Kelas : TI Semester 4
# Tugas : Class Method dan Static Method


class Mahasiswa:
    universitas = "Universitas Nusa Putra"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # Instance Method
    def tampilkan_data(self):
        print("\n=== Data Mahasiswa ===")
        print("Nama        :", self.nama)
        print("Umur        :", self.umur)
        print("Universitas :", Mahasiswa.universitas)

    # Class Method
    @classmethod
    def ubah_universitas(cls, universitas_baru):
        cls.universitas = universitas_baru

    # Static Method
    @staticmethod
    def cek_dewasa(umur):
        return umur >= 18


# Membuat objek mahasiswa
mhs1 = Mahasiswa("Rassya", 20)
mhs2 = Mahasiswa("Andi", 17)

# Menampilkan data awal
mhs1.tampilkan_data()
mhs2.tampilkan_data()

# Menggunakan Static Method
print("\n=== Pengecekan Umur ===")
print("Rassya Dewasa :", Mahasiswa.cek_dewasa(mhs1.umur))
print("Andi Dewasa   :", Mahasiswa.cek_dewasa(mhs2.umur))

# Menggunakan Class Method
Mahasiswa.ubah_universitas("Universitas Indonesia")

print("\n=== Setelah Universitas Diubah ===")
mhs1.tampilkan_data()
mhs2.tampilkan_data()