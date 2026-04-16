#Praktikum 1: Membuat dan Menggunakan Fungsi

# Fungsi Built-in
# Fungsi print() adalah contoh fungsi built-in untuk mencetak output 
print("Ini adalah contoh fungsi built-in")

# Fungsi len() adalah contoh fungsi built-in untuk menghitung panjang suatu objek
kata = "Pemrograman"
panjang_kata = len(kata)
print(f"Panjang kata '{kata}' adalah: {panjang_kata}") 

# Fungsi max() adalah contoh fungsi built-in untuk mencari nilai maksimum dari sebuah daftar
angka = [10, 5, 30, 40, 25]
nilai_max = max(angka)
print(f"Nilai maksimum dalam daftar {angka} adalah: {nilai_max}")

# Fungsi User-Defined
# Fungsi dengan satu parameter (Menerima satu nilai input) 
def cetak_kuadrat(angka):
    # Menghitung kuadrat dari angka yang diterima sebagai parameter
    print(f"Kuadrat dari {angka} adalah: {angka ** 2}") 

# Fungsi dengan beberapa parameter (Menerima lebih dari satu nilai input) 
def hitung_luas_persegi_panjang(panjang, lebar):
    # Menghitung luas persegi panjang
    return panjang * lebar

# Fungsi dengan beberapa tipe parameter (Menerima berbagai jenis data)
def info_mahasiswa(nama, umur, ipk):
    # Mencetak informasi mahasiswa
    print(f"Nama: {nama}, Umur: {umur}, IPK: {ipk}") 

# Fungsi tanpa return value (Non-return value)
def sapa_pengguna(nama):
    # Fungsi ini hanya mencetak sapaan tanpa mengembalikan nilai
    print(f"Halo, {nama}! Selamat datang di dunia Python.")

# Fungsi dengan return value
def hitung_keliling_persegi(sisi):
    # Mengembalikan keliling persegi 
    return 4 * sisi

# Pemanggilan fungsi dengan satu parameter
cetak_kuadrat(5)

# Pemanggilan fungsi dengan beberapa parameter 
luas = hitung_luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang: {luas}") 

# Pemanggilan fungsi dengan beberapa tipe parameter 
info_mahasiswa("Budi", 22, 3.8)

# Pemanggilan fungsi tanpa return value 
sapa_pengguna("Andi")

# Pemanggilan fungsi dengan return value 
keliling = hitung_keliling_persegi(5)
print(f"Keliling persegi dengan sisi 5 adalah: {keliling}") 


#Praktikum 3: Membuat Kelas Sederhana

# Kelas Buku untuk merepresentasikan buku di perpustakaan 
class Buku:
    def  __init__(self, judul, pengarang, tahun_terbit): 
       self.judul = judul
       self.pengarang = pengarang
       self.tahun_terbit = tahun_terbit
       self.status = "Tersedia" # Status buku, default adalah Tersedia  
    
    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}") 
        print(f"Status: {self.status}")

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            print(f"Buku '{self.judul}' telah dipinjam.") 
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.") 

    def kembalikan(self):
        if self.status == "Dipinjam":
            self.status = "Tersedia"
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' tidak sedang dipinjam.") 

# Membuat objek dari kelas Buku

buku1 = Buku("Pemrograman Python", "John Doe", 2021)
buku2 = Buku("Data Science untuk Pemula", "Jane Smith", 2020)

# Menggunakan metode objek Buku 
buku1.tampilkan_info()
buku2.pinjam()

# Mengubah status buku dan menampilkan informasi 
buku2.kembalikan()
buku1.pinjam()
buku1.tampilkan_info()

# Kelas Mahasiswa untuk merepresentasikan Mahasiswa dalam kelas

# Definisi kelas 
class Mahasiswa:
    # Konstruktor (  init  ) untuk menginisialisasi atribut objek
    def __init__(self, nama, nim, umur):
        self.nama = nama # Atribut objek nama 
        self.nim = nim	# Atribut objek nim 
        self.umur = umur # Atribut objek umur 

    # Metode untuk menampilkan informasi mahasiswa 
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Umur: {self.umur} tahun")

    # Metode untuk merubah umur mahasiswa 
    def ubah_umur(self, umur_baru):
        self.umur = umur_baru 

        # Membuat objek (instance) dari kelas Mahasiswa 
mahasiswa1 = Mahasiswa("Andi", "12345", 20)
mahasiswa2 = Mahasiswa("Budi", "67890", 22)
# Menggunakan metode dari kelas Mahasiswa 
mahasiswa1.tampilkan_info()
print() # Baris kosong
mahasiswa2.tampilkan_info()

 # Mengubah umur mahasiswa1 menggunakan metode ubah_umur 
mahasiswa1.ubah_umur(21)

# Menampilkan info mahasiswa setelah umur diubah 
print("\nSetelah mengubah umur mahasiswa1:")
mahasiswa1.tampilkan_info()


#Praktikum 4: Membuat dan Menggunakan Method dalam Kelas

# Kelas untuk menjelaskan atribut dan metode dalam kelas 
class Mobil:
    def __init__(self, merk, warna, tahun, harga): 
        # Atribut yang dimiliki oleh objek Mobil 
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        self.harga = harga 

        # Fungsi tanpa return value, hanya mencetak informasi
    def tampilkan_info(self):
         print(f"Mobil {self.merk} berwarna {self.warna}, tahun {self.tahun}, harga: Rp {self.harga}")

    # Fungsi dengan satu parameter
    def diskon(self, persen_diskon):
            # Menghitung harga setelah diskon
            diskon_harga = self.harga * (persen_diskon / 100) 
            harga_setelah_diskon = self.harga - diskon_harga
            print(f"Harga setelah diskon {persen_diskon}%: Rp {harga_setelah_diskon}")
            # Tidak mengembalikan nilai, hanya mencetak harga setelah diskon 

    # Fungsi dengan return value, menghitung usia mobil berdasarkan tahun
    def hitung_usia(self, tahun_sekarang):
        usia = tahun_sekarang - self.tahun 
        return usia
        
    # Fungsi dengan beberapa parameter
    def perbarui_harga(self, harga_baru, tahun_baru):
        self.harga = harga_baru
        self.tahun = tahun_baru
        print(f"Harga dan tahun mobil {self.merk} diperbarui menjadi Rp {self.harga} dan tahun {self.tahun}")

# Membuat objek mobil
mobil1 = Mobil("Toyota", "Hitam", 2015, 300000000)
mobil2 = Mobil("Honda", "Merah", 2018, 250000000)

# Menggunakan metode tanpa return value
mobil1.tampilkan_info()
mobil2.tampilkan_info()

# Menggunakan metode dengan satu parameter (diskon) 
mobil1.diskon(10)
mobil2.diskon(15)

# Menggunakan metode dengan return value (hitung usia mobil) 
usia_mobil1 = mobil1.hitung_usia(2025)
usia_mobil2 = mobil2.hitung_usia(2025) 

print(f"Usia mobil1 pada tahun 2025: {usia_mobil1} tahun") 
print(f"Usia mobil2 pada tahun 2025: {usia_mobil2} tahun")

# Menggunakan metode dengan beberapa parameter (perbarui harga dan tahun
mobil1.perbarui_harga(280000000, 2022)
mobil2.perbarui_harga(240000000, 2021)



#Penugasan 01 (Jadwal kelas)
# --- main.py ---

# Mengimport semua fungsi dan kelas dari file manajemen_kuliah
import manajemen_kuliah as mk

def main():
    jadwal_saya = []
    
    while True:
        print("\n=== Sistem Manajemen Jadwal Kuliah ===")
        print("1. Lihat Jadwal")
        print("2. Tambah Jadwal")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            mk.lihat_semua_jadwal(jadwal_saya) # Memanggil fungsi dari modul
        elif pilihan == '2':
            mk.tambah_jadwal(jadwal_saya)      # Memanggil fungsi dari modul
        elif pilihan == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()