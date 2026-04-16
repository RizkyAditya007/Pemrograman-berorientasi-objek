# --- manajemen_kuliah.py ---

class MataKuliah:
    def __init__(self, kode, nama, dosen, hari, jam):
        self.kode = kode
        self.nama = nama
        self.dosen = dosen
        self.hari = hari
        self.jam = jam

    def tampilkan_info(self):
        return f"[{self.kode}] {self.nama.ljust(20)} | {self.hari}, {self.jam} | Dosen: {self.dosen}"

def tambah_jadwal(daftar_jadwal):
    print("\n--- Tambah Mata Kuliah Baru ---")
    kode = input("Masukkan Kode MK: ")
    nama = input("Masukkan Nama MK: ")
    dosen = input("Masukkan Nama Dosen: ")
    hari = input("Masukkan Hari: ")
    jam = input("Masukkan Jam: ")
    
    mk_baru = MataKuliah(kode, nama, dosen, hari, jam)
    daftar_jadwal.append(mk_baru)
    print("Jadwal berhasil ditambahkan!")

def lihat_semua_jadwal(daftar_jadwal):
    print("\n" + "="*70)
    print("DAFTAR JADWAL KULIAH")
    print("="*70)
    if not daftar_jadwal:
        print("Belum ada jadwal yang tersimpan.")
    else:
        for index, jadwal in enumerate(daftar_jadwal, start=1):
            print(f"{index}. {jadwal.tampilkan_info()}")
    print("="*70)