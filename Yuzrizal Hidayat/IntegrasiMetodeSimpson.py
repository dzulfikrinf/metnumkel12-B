from math import e

# Fungsi untuk melakukan integrasi metode Simpson 1/3
def simpson_one_third(func, a, b, n):
    if n % 2 != 0:  
        # Cek apakah jumlah subinterval (n) genap, karena metode Simpson 1/3 membutuhkan jumlah subinterval genap.
        print("Jumlah subinterval harus genap untuk metode Simpson 1/3.")
        return None

    h = (b - a) / n
    integral = func(a) + func(b)

    # Iterasi untuk subinterval dengan indeks ganjil
    for i in range(1, n, 2):
        integral += 4 * func(a + i * h)  

    # Iterasi untuk subinterval dengan indeks genap (kecuali yang terakhir)
    for i in range(2, n - 1, 2):
        integral += 2 * func(a + i * h)  

    integral *= h / 3

    return integral

# Input fungsi dari pengguna
def input_function():
    func_str = input("Masukkan fungsi yang ingin diintegralkan (gunakan x sebagai variabel): ")
    try:
        # Menggunakan lambda untuk membuat fungsi dari string input pengguna
        func = lambda x: eval(func_str) 
        return func
    except Exception as e:
        print("Terjadi kesalahan dalam membaca fungsi. Pastikan input fungsi benar.")
        print(e)
        return input_function()

# Input batas bawah, batas atas, dan jumlah partisi dari pengguna
a = float(input("Masukkan batas bawah integral: "))
b = float(input("Masukkan batas atas integral: "))
n = int(input("Masukkan jumlah partisi: "))

# Meminta pengguna memasukkan fungsi
fungsi = input_function()

# Menghitung hasil integrasi metode Simpson 1/3
hasil_integrasi = simpson_one_third(fungsi, a, b, n)

# Menampilkan hasil integrasi
if hasil_integrasi is not None:
    print(f"Hasil integrasi metode Simpson 1/3 dari {a} hingga {b} dengan {n} subinterval adalah: {hasil_integrasi}")
