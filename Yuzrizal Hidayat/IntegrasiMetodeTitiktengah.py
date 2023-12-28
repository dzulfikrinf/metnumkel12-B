from math import e

# Fungsi untuk melakukan integrasi metode titik tengah
def midpoint_rule(func, a, b, n):
    # Menghitung lebar setiap subinterval
    h = (b - a) / n
    integral = 0.0

    # Menghitung nilai integral dengan menggunakan titik tengah setiap subinterval
    for i in range(n):
        # Menentukan titik tengah subinterval
        mid_point = (a + h / 2.0) + i * h
        # Menambahkan kontribusi titik tengah ke integral
        integral += func(mid_point)

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

# Input batas bawah, batas atas, dan jumlah partisi dari pengguna
a = float(input("Masukkan batas bawah integral: "))
b = float(input("Masukkan batas atas integral: "))
n = int(input("Masukkan jumlah partisi: "))

# Meminta pengguna memasukkan fungsi
fungsi = input_function()

# Menghitung hasil integrasi metode titik tengah
hasil_integrasi = midpoint_rule(fungsi, a, b, n)

# Menampilkan hasil integrasi
print(f"Hasil integrasi metode titik tengah dari {a} hingga {b} dengan {n} subinterval adalah: {hasil_integrasi}")
