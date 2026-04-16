#Praktikum 01: Enkapsulasi pada kelas Bank Account

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner 
        self.__balance = balance
    def	deposit(self, amount):
        """Method untuk menambahkan saldo."""
        if amount > 0:
            self.__balance += amount
            print(f"{amount} telah ditambahkan ke akun {self.__owner}.")
        else:
            print("Jumlah deposit harus lebih dari 0.")
    def	withdraw(self, amount):
        """Method untuk menarik saldo."""
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} telah ditarik dari akun {self.__owner}.")
        else:
            print("Saldo tidak mencukupi.")
    def	get_balance(self):
        """Method untuk mendapatkan informasi saldo terkini."""
        return self.__balance

# Contoh penggunaan
if __name__== "__main__":
    alice_account = BankAccount(owner="Alice", balance=1000)

    # Deposit uang
    alice_account.deposit(500)	# Berhasil
    alice_account.deposit(-100)	# Gagal (validasi)

    # Withdraw uang
    alice_account.withdraw(300)	# Berhasil
    alice_account.withdraw(2000)	# Gagal (saldo tidak cukup)

    # Mendapatkan saldo
    current_balance = alice_account.get_balance()
    print(f"Saldo terakhir di akun {alice_account._BankAccount__owner}:{current_balance}")


#Praktikum 02: Enkapsulasi pada kelas Employee

class Employee:
    def __init__(self, name, salary):
        # Atribut privat dengan double underscore
        self.__name = name
        self.__salary = salary

    def update_salary(self, increase):
        """Method untuk menaikkan gaji dengan validasi."""
        if increase > 0:
            self.__salary += increase
            print(f"Gaji telah dinaikkan sebesar {increase}.")
        else:
            print("Nilai kenaikan harus lebih dari 0.")

    def set_salary(self, new_salary):
        """Method untuk mengubah gaji dengan validasi."""
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Gaji diatur ulang menjadi {new_salary}.")
        else:
            print("Gaji tidak dapat bernilai negatif.")

    def get_salary(self):
        """Method untuk mendapatkan informasi gaji."""
        return self.__salary

    def get_employee_info(self):
        """Method untuk menampilkan informasi karyawan secara menyeluruh."""
        return f"Employee: {self.__name}, Gaji: {self.__salary}"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek Employee dengan nama "John Doe" dan gaji awal 50000
    employee1 = Employee("John Doe", 50000)

    # Tampilkan informasi karyawan
    print(employee1.get_employee_info())

    # Update gaji dengan menaikkan sebesar 5000
    employee1.update_salary(5000)
    print(f"Gaji setelah kenaikan: {employee1.get_salary()}")

    # Atur ulang gaji dengan nilai baru
    employee1.set_salary(60000)
    print(f"Informasi terbaru: {employee1.get_employee_info()}")

    # Mencoba mengakses atribut privat secara langsung (tidak direkomendasikan)
    # Contoh: print(employee1.__salary)  --> Ini akan menimbulkan error


#Praktikum 03: Konstruktor dan Destruktor Sederhana

class SimpleExample:
    def __init__(self, name):
        """
        Konstruktor: Dipanggil saat objek dibuat.
        Menyimpan nilai 'name' dan mencetak pesan pembuatan objek.
        """
        self.name = name
        print(f"Konstruktor: Objek '{self.name}' telah dibuat.")

    def __del__(self):
        """
        Destruktor: Dipanggil saat objek dihapus.
        Mencetak pesan bahwa objek sedang dihapus.
        """
        print(f"Destruktor: Objek '{self.name}' sedang dihapus.")

def main():
    print("Program dimulai.\n")

    # Membuat objek SimpleExample
    obj = SimpleExample("Demo")
    print("Program sedang berjalan...\n")

    # Menghapus objek secara eksplisit
    del obj
    print("Objek telah dihapus secara eksplisit.\n")

    print("Program selesai.")

if __name__ == "__main__":
    main()


#Praktikum 04: Konstruktor dan Destruktor program FileLogger

class FileLogger:
    def __init__(self, filename):
        """
        Konstruktor: Membuka file log untuk menulis pesan.
        Parameter:
            - filename: Nama file tempat pesan log akan ditulis.
        """
        self.filename = filename
        try:
            self.file = open(filename, "a")  # Membuka file dalam mode append
            print(f"File '{filename}' berhasil dibuka untuk logging.")
        except Exception as e:
            print(f"Gagal membuka file '{filename}': {e}")

    def write_log(self, message):
        """
        Menulis pesan log ke dalam file.
        Parameter:
            - message: Pesan yang akan ditulis ke file.
        """
        self.file.write(message + "\n")
        self.file.flush()  # Memastikan pesan langsung ditulis ke disk
        print(f"Pesan log: '{message}' telah ditulis.")

    def __del__(self):
        """
        Destruktor: Menutup file log ketika objek dihapus.
        """
        if hasattr(self, "file") and not self.file.closed:
            self.file.close()
            print(f"File '{self.filename}' telah ditutup.")

# Contoh penggunaan dalam skenario nyata aplikasi
if __name__ == "__main__":
    # Membuat objek logger untuk file "application.log"
    logger = FileLogger("application.log")

    # Menulis beberapa pesan log selama operasi aplikasi
    logger.write_log("Aplikasi dimulai.")
    logger.write_log("Melakukan operasi A...")
    logger.write_log("Operasi A selesai.")
    logger.write_log("Aplikasi akan segera selesai.")

    # Menghapus objek logger secara eksplisit
    del logger

    # Jika objek tidak dihapus secara eksplisit, destruktor akan dipanggil
    # ketika program berakhir dan garbage collection membersihkan objek tersebut.


#Praktikum 05: Properti "self" pada kelas

class Calculator:
    def __init__(self, initial_value=0):
        """
        Konstruktor kelas Calculator.
        - self: Mengacu pada instance yang dibuat.
        - initial_value: Nilai awal dari kalkulator.
        """
        self.value = initial_value
        print(f"Kalkulator diinisialisasi dengan nilai: {self.value}")

    def add(self, number):
        """
        Menambahkan 'number' ke nilai yang tersimpan di objek.
        - self.value: Menunjukkan nilai saat ini yang disimpan di objek tersebut.
        - number: Nilai yang akan ditambahkan.
        """
        self.value += number
        print(f"Setelah penambahan {number}, nilai sekarang adalah: {self.value}")

    def subtract(self, number):
        """
        Mengurangi 'number' dari nilai yang tersimpan.
        - self.value: Nilai saat ini dalam objek.
        - number: Nilai yang akan dikurangkan.
        """
        self.value -= number
        print(f"Setelah pengurangan {number}, nilai sekarang adalah: {self.value}")

    def reset(self):
        """
        Mengatur ulang nilai kalkulator ke 0.
        """
        self.value = 0
        print("Nilai telah direset ke 0.")

    def show_value(self):
        """
        Menampilkan nilai saat ini dari kalkulator.
        """
        print(f"Nilai saat ini adalah: {self.value}")

# Contoh penggunaan untuk memahami peran 'self'
def main():
    # Membuat objek Calculator dengan nilai awal 10
    calc1 = Calculator(initial_value=10)

    # Menggunakan metode dari objek calc1
    calc1.add(5)          # Menambah 5 ke nilai calc1
    calc1.subtract(3)     # Mengurangi 3 dari nilai calc1
    calc1.show_value()    # Menampilkan nilai calc1

    # Membuat objek Calculator lainnya dengan nilai awal default (0)
    calc2 = Calculator()
    calc2.add(20)         # Menambah 20 ke nilai calc2
    calc2.show_value()    # Menampilkan nilai calc2

    # Penjelasan peran self:
    # 'self' memungkinkan setiap instance (calc1, calc2) memiliki atribut 'value' masing-masing.
    # Perubahan yang dilakukan pada calc1 tidak akan mempengaruhi calc2, karena masing-masing
    # mengacu pada self yang berbeda (instance yang berbeda).

if __name__ == "__main__":
    main()


#Praktikum 06: Menggunakan getter, setter, dan dekorator @property untuk mengelola akses atribut

class Person:
    def __init__(self, name, age):
        """
        Konstruktor untuk menginisialisasi objek Person dengan nama dan umur.
        Atribut privat (dengan double underscore) menyimpan data internal.
        """
        self.__name = name
        self.__age = age

    @property
    def name(self):
        """
        Getter untuk atribut name.
        Mengembalikan nilai dari __name.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Setter untuk atribut name.
        Memeriksa apakah nilai tidak kosong sebelum mengubah nilai __name.
        """
        if not value:
            print("Nama tidak boleh kosong.")
        else:
            self.__name = value

    @property
    def age(self):
        """
        Getter untuk atribut age.
        Mengembalikan nilai dari __age.
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Setter untuk atribut age.
        Memeriksa apakah nilai umur tidak negatif sebelum mengubah nilai __age.
        """
        if value < 0:
            print("Umur tidak boleh negatif!")
        else:
            self.__age = value

# Contoh penggunaan
def main():
    # Membuat objek Person dengan nama "Alice" dan umur 30
    person = Person("Alice", 30)
    print(f"Nama: {person.name}, Umur: {person.age}")

    # Mengubah nama dan umur melalui setter
    person.name = "Bob"
    person.age = 35
    print(f"Nama baru: {person.name}, Umur baru: {person.age}")

    # Mencoba menetapkan nilai yang tidak valid untuk umur
    person.age = -5  # Akan memunculkan pesan error karena validasi umur negatif

if __name__ == "__main__":
    main()



#Penugasan 01 kelas Python bernama Student.

class Student:
    def __init__(self, name, score):
        # Atribut privat dengan double underscore
        self.__name = name
        self.__score = None  # Inisialisasi awal
        self.__grade = None
        
        # Menggunakan setter untuk validasi score dan penentuan grade otomatis
        self.score = score

    # Getter untuk name
    @property
    def name(self):
        return self.__name

    # Setter untuk name
    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            print("Nama tidak boleh kosong.")

    # Getter untuk score
    @property
    def score(self):
        return self.__score

    # Setter untuk score dengan validasi dan update grade otomatis
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
            self.__update_grade()  # Memanggil method internal untuk update grade
        else:
            print("Validasi score gagal: harus berada di antara 0 hingga 100.")

    # Getter untuk grade (hanya baca, tidak ada setter)
    @property
    def grade(self):
        return self.__grade

    # Method internal untuk menentukan grade berdasarkan score
    def __update_grade(self):
        if self.__score >= 90:
            self.__grade = 'A'
        elif self.__score >= 80:
            self.__grade = 'B'
        elif self.__score >= 70:
            self.__grade = 'C'
        elif self.__score >= 60:
            self.__grade = 'D'
        else:
            self.__grade = 'E'

    def show_info(self):
        """Menampilkan informasi lengkap mahasiswa."""
        print(f"Nama Mahasiswa: {self.name}")
        print(f"Nilai: {self.score}")
        print(f"Grade: {self.grade}")

    def __del__(self):
        """Destruktor yang dipanggil saat objek dihapus."""
        print(f"Data mahasiswa {self.__name} telah dihapus dari sistem.")

# --- Contoh Penggunaan (Sesuai Output yang Diharapkan) ---
if __name__ == "__main__":
    # Membuat objek mahasiswa
    mhs = Student("Siti", 87)
    mhs.show_info()

    print("\nNilai diubah...")
    # Mengubah nilai melalui setter
    mhs.score = 93
    mhs.show_info()
    
    print() # Baris baru sebelum destruktor terpanggil otomatis di akhir program