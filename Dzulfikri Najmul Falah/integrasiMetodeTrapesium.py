from math import e # import e supaya nilai e dapat terdeteksi oleh program

# Fungsi untuk melakukan integrasi metode trapesium
def trapesium_method(func, a, b, n):
    h = (b - a) / n
    integral = (func(a) + func(b)) / 2.0

    for i in range(1, n):
        integral += func(a + i * h)

    integral *= h

    return integral

# Input fungsi dari pengguna
def input_function():
    func_str = input("Masukkan fungsi yang ingin diintegralkan (gunakan x sebagai variabel): ")
    try:
        func = lambda x: eval(func_str)
        return func
    except Exception as e:
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
hasil_integrasi = trapesium_method(fungsi, a, b, n)

# Menampilkan hasil integrasi
print(f"Hasil integrasi metode trapesium dari {a} hingga {b} dengan {n} partisi adalah: {hasil_integrasi}")
