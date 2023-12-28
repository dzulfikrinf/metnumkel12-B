from math import e # Import e supaya nilai e dapat terdeteksi oleh program

# Fungsi untuk melakukan integrasi metode trapesium
def trapezoidal_method(func, a, b, n):
    # Menghitung lebar setiap subinterval
    h = (b - a) / n
    # Menginisialisasi nilai integral dengan nilai trapesium pertama
    integral = (func(a) + func(b)) / 2.0

    # Menambahkan kontribusi trapesium dari setiap subinterval
    for i in range(1, n):
        integral += func(a + i * h)

    # Mengalikan hasil dengan lebar subinterval untuk mendapatkan nilai integral total
    integral *= h

    return integral

# Input fungsi dari pengguna
def input_function():
    # Meminta pengguna memasukkan fungsi sebagai string
    func_str = input("Masukkan fungsi yang ingin diintegralkan (gunakan x sebagai variabel): ")
    try:
        # Menggunakan lambda untuk membuat fungsi dari string input pengguna
        func = lambda x: eval(func_str)
        return func
    except Exception as e:
        # Menangani kesalahan jika input fungsi tidak valid
        print("Terjadi kesalahan dalam membaca fungsi. Pastikan input fungsi benar.")
        print(e)
        return input_function()

# Input batas bawah, batas atas, dan jumlah partisi (n) dari pengguna
a = float(input("Masukkan batas bawah integral: "))
b = float(input("Masukkan batas atas integral: "))
n = int(input("Masukkan jumlah partisi (n): "))

# Meminta pengguna memasukkan fungsi
fungsi = input_function()

# Menghitung hasil integrasi metode trapesium
hasil_integrasi = trapezoidal_method(fungsi, a, b, n)

# Menampilkan hasil integrasi
print(f"Hasil integrasi metode trapesium dari {a} hingga {b} dengan {n} partisi adalah: {hasil_integrasi}")
