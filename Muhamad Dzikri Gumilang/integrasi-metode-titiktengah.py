from math import e

# Fungsi menjalankan integrasi metode titik tengah
def midpoint_rule(func, a, b, n):
    h = (b - a) / n
    integral = 0.0

    # Menghitung nilai integral dengan titik tengah setiap subinterval
    for i in range(n):
        mid_point = (a + h / 2.0) + i * h
        integral += func(mid_point)

    integral *= h

    return integral

# Input fungsi 
def input_function():
    func_str = input("Masukkan fungsi yang ingin diintegralkan (gunakan x sebagai variabel): ")
    try:
        func = lambda x: eval(func_str) 
        return func
    except Exception as e:
        print("Terjadi kesalahan dalam membaca fungsi. Pastikan input fungsi benar.")
        print(e)
        return input_function()

# Input batas bawah, batas atas, dan jumlah partisi 
a = float(input("Masukkan batas bawah integral: "))
b = float(input("Masukkan batas atas integral: "))
n = int(input("Masukkan jumlah partisi: "))

# User diminta memasukkan fungsi
fungsi = input_function()

# Menghitung hasil integrasi metode titik tengah
hasil_integrasi = midpoint_rule(fungsi, a, b, n)

# Cetak hasil integrasi
print(f"Hasil integrasi metode titik tengah dari {a} hingga {b} dengan {n} subinterval adalah: {hasil_integrasi}")
