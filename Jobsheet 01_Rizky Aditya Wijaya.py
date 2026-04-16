#Praktikum 01 Tipe data dasar

# 1. Number (int, float, complex)
# integer (int)
angka_int = 10
print("angka_int =", angka_int, "->", type(angka_int))

# Float
angka_float = 3.14
print("angka_float =", angka_float, "->", type(angka_float))

# Complex
angka_complex = 2 + 3j
print("angka_complex =", angka_complex, "->", type(angka_complex)) 

# 2. Boolean
is_active = True
print("is_active =", is_active, "->", type(is_active))

# 3. String
teks = "Hello, Python!"
print("teks =", teks, "->", type(teks))

# 4. List
# List adalah tipe data terurut dan dapat diubah (mutable)
daftar_angka = [1, 2, 3, 4, 5]
print("daftar_angka =", daftar_angka, "->", type(daftar_angka))

# 5. Tuple
# Tuple adalah tipe data terurut tetapi tidak dapat diubah (immutable)
koordinat = (10, 20)
print("koordinat =", koordinat, "->", type(koordinat))

# 6. Dictionary
# Dictionary menyimpan data dalam pasangan key-value
data_mahasiswa = {
    "nama": "Andi",
    "nim": "A11.2022.12345",
    "jurusan": "Teknik Informatika"
}

print("data_mahasiswa =", data_mahasiswa, "->", type(data_mahasiswa))

# 7. Set
# Set adalah tipe data yang tidak terurut, unik (tiap elemen hanya muncul 1x)
himpunan_angka = {1, 2, 3, 2, 1}
print("himpunan_angka =", himpunan_angka, "->", type(himpunan_angka))

# 8. Contoh penggunaan konversi tipe data
nilai_str = "100"
print("\nnilai_str =", nilai_str, "->", type(nilai_str)) 
nilai_int = int(nilai_str)  # konversi string ke integer 
print("nilai_int =", nilai_int, "->", type(nilai_int))


#Praktikum 02. Variabel dan Operasi dasar

# -*- coding: utf-8 -*- 

# 1. Pendeklarasian Variabel 
nama = "Budi"
umur = 20
tinggi = 170.5
is_student = True

print("Nama =", nama)
print("Umur =", umur)
print("Tinggi =", tinggi, "cm") 
print("Mahasiswa =", is_student) 

# Python tidak memerlukan deklarasi tipe data secara eksplisit. # Tipe data variabel akan menyesuaikan nilai yang diberikan.
# 2. Operasi Aritmetika
a = 10
b = 3
penjumlahan = a + b # Tambah
pengurangan = a - b # Kurang
perkalian = a * b # Kali
pembagian = a / b # Bagi (hasil float)
pembagian_bulat = a // b # Bagi (bulat)
modulus = a % b # Sisa bagi
pangkat = a ** b # Pemangkatan
print("\nOPERASI ARITMETIKA")
print("a =", a, ", b =", b)
print("Penjumlahan", penjumlahan)
print("Pengurangan =", pengurangan)
print("Perkalian =", perkalian)
print("Pembagian =", pembagian)
print("Pembagian Bulat =", pembagian_bulat)
print("Modulus =", modulus)
print ("Pangkat =", pangkat)

# 3. Operasi Perbandingan
# Menghasilkan nilai Boolean (True/False)
lebih_besar = a > b
kurang_dari = a < b
sama_dengan = a == b
tidak_sama = a != b
lebih_besar_sama = a >= b
kurang_sama = a <= b
print("\nOPERASI PERBANDINGAN")
print("a > b =", lebih_besar)
print("a < b =", kurang_dari)
print("a == b =", sama_dengan)
print("a != b =", tidak_sama)
print("a >= b =", lebih_besar_sama)
print("a <= b =", kurang_sama)

# 4. Operasi Logika 
# and, or, not
x = True 
y = False

logika_and = x and y
logika_or = x or y
logika_not_x = not x 

print("\nOPERASI LOGIKA")
print("x =", x, ", y =", y)
print("x and y =", logika_and) 
print("x or y =", logika_or) 
print("not x =", logika_not_x) 

# 5. Contoh penggunaan di dalam percabangan 
if a > b and b > 0:
    print("\nKondisi terpenuhi: a lebih besar dari b, dan b masih positif.")
else:
     print("\nKondisi tidak terpenuhi atau b <= 0.")


# Praktikum 03. Percabangan

# -*- coding: utf-8 -*- 

# 1. IF Sederhana
# Program hanya mengeksekusi blok jika kondisinya True 

nilai = 85
print("Contoh IF Sederhana:") 
if nilai > 80:
     print("Selamat! Anda lulus dengan nilai tinggi.\n")

# 2. IF-ELSE
# Jika kondisi True, eksekusi blok if; jika False, eksekusi blok else 
umur = 17
print("Contoh IF-ELSE:")
if umur >= 18:
     print("Anda sudah cukup umur untuk mendapatkan SIM.") 
else:
     print("Anda belum cukup umur untuk mendapatkan SIM.\n") 

# 3. IF-ELIF-ELSE
# Menangani banyak kondisi secara berurutan.
# Jika ada kondisi yang terpenuhi, blok yang bersangkutan dieksekusi,
# lalu program melewati blok kondisi setelahnya.

hari = "Rabu"
print("Contoh IF-ELIF-ELSE:") 
if hari == "Senin":
     print("Hari Senin - Saatnya kembali bekerja!") 
elif hari == "Selasa":
     print("Hari Selasa - Jadwal rapat mingguan.")
elif hari == "Rabu": 
     print("Hari Rabu - Ada diskon di beberapa toko.") 
else:
     print("Hari lainnya - Atur jadwalmu dengan baik.\n") 

# 4. IF Bersarang (Nested IF)
#Kondisi di dalam kondisi, biasa digunakan jika kita perlu
# memeriksa sub-kondisi setelah kondisi pertama terpenuhi.
suhu = 35
print("Contoh IF Bersarang (Nested IF):")
if suhu > 30:
     print("Cuaca cukup panas.")
     if suhu > 40:
          print ("Bahkan sangat terik! Disarankan banyak minum air.")
     else:
          print("Masih relatif normal, tapi tetap jaga kesehatan.")
else:
     print("Cuaca sepertinya cukup sejuk.\n")

#5. Menggabungkan Percabangan dengan Operasi Logika
# Memeriksa beberapa kondisi sekaligus dengan and, or, not

nilai_teori = 75
nilai_praktik = 80
print("Contoh IF dengan Operasi Logika AND/OR:")
if nilai_teori >= 70 and nilai_praktik >= 70:
     print("Anda lulus karena nilai teori dan praktik memadai.")
elif nilai_teori < 70 and nilai_praktik < 70:
     print("Anda perlu meningkatkan nilai teori dan praktik.") 
elif nilai_teori < 70:
     print("Anda perlu meningkatkan nilai teori.")
else:
     print("Anda perlu meningkatkan nilai praktik.\n")

# 6. Penggunaan If Ternary (atau Conditional Expression)
# Bentuk ringkas: <hasil_if_true> if <kondisi> else <hasil_if_false>

angka = -5
print("Contoh If Ternary (Conditional Expression):") 
status = "Positif" if angka > 0 else "Negatif atau Nol" 
print("Angka =", angka, "=>", status)


#Praktikum 04. Perulangan

# -*- coding: utf-8 -*- 

# 1. FOR Loop dengan range()
print("1) FOR loop dengan range()") 
for i in range(5):
    print("Perulangan ke-", i)
# range(5) menghasilkan nilai 0, 1, 2, 3, dan 4
# Sehingga perulangan akan berjalan sebanyak 5 kali 

print() # pemisah output 11:

# 2. FOR Loop untuk mengiterasi List 
print("2) FOR loop mengiterasi list")
buah = ["apel", "mangga", "jeruk", "pisang"] 
for item in buah:
     print("Buah:", item)
# Loop akan mengeksekusi setiap elemen dalam list "buah" 

print()

# 3. WHILE Loop
print("3) WHILE loop sederhana") 
count = 0
while count < 5:
     print("count =", count)
     count += 1 # increment
# Perulangan while terus dijalankan selama kondisi (count < 5) bernilai True

print()

# 4. BREAK pada Loop
print("4) BREAK di dalam loop") 
for i in range(10):
     if i == 3:
          print("Loop dihentikan pada i =", i)
          break # mengakhiri loop saat i = 3 
     print("i =", i)
# Keyword break langsung menghentikan keseluruhan perulangan 

print()

# 5. CONTINUE pada Loop
print("5) CONTINUE di dalam loop") 
for i in range(5):
     if i == 2:
          print("Lewati i =", i, "dengan continue")
          continue # melewati iterasi saat ini dan lanjut ke iterasi berikutnya
     print("i =", i)
# Saat i = 2, baris print("i =", i) tidak akan dieksekusi 

print()

# 6. NESTED Loop (Loop Bersarang) 
print("6) NESTED loop")
for i in range(3):
     for j in range(2):
          print(f"i={i}, j={j}")
# Pada setiap iterasi i, loop j akan berjalan dari 0 sampai 1 

print()

# 7. Memanfaatkan ELSE pada Loop
print("7) ELSE pada loop for/while")
# Python memiliki fitur unik: blok else pada loop
# Blok else akan dieksekusi jika loop selesai tanpa di-break. 

for x in range(3):
     print("x =", x) 
else:
     print("Loop for telah selesai tanpa break.\n")

y = 0
while y < 3:
     print("y =", y)
     y += 1
else:
     print("Loop while telah selesai tanpa break.\n") 

# 8. PASS sebagai placeholder
print("8) PASS (placeholder)") 
for i in range(3):
     if i == 1:
          pass # pass tidak melakukan apa-apa, digunakan sebagai placeholder 
     print("i =", i)



#Penugasan 1
# Program Penghitung BMI

berat = float(input("Masukkan berat badan (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

tinggi_m = tinggi_cm / 100

bmi = berat / (tinggi_m ** 2)

if bmi < 18.5:
    kategori = "Underweight"
elif 18.5 <= bmi <= 24.9:
    kategori = "Normal"
elif 25 <= bmi <= 29.9:
    kategori = "Overweight"
else:
    kategori = "Obesity"

print("-" * 30)
print(f"Nilai BMI Anda: {bmi:.2f}")
print(f"Kategori: {kategori}")
print("-" * 30)

#Penugasan 2
#Program yang mengecek apakah suatu bilangan genap, ganjil, atau prima.

def cek_bilangan():
    try:
        angka = int(input("Masukkan sebuah bilangan bulat positif: "))
        
        if angka < 0:
            print("Silakan masukkan bilangan bulat positif.")
            return

        if angka % 2 == 0:
            status_genap_ganjil = "Genap"
        else:
            status_genap_ganjil = "Ganjil"

        is_prima = True
        if angka < 2:
            is_prima = False
        else:
            for i in range(2, int(angka**0.5) + 1):
                if angka % i == 0:
                    is_prima = False
                    break
        
        status_prima = "Bilangan Prima" if is_prima else "Bukan Bilangan Prima"

        print(f"\nAngka {angka} adalah:")
        print(f"- {status_genap_ganjil}")
        print(f"- {status_prima}")

    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.")

cek_bilangan()