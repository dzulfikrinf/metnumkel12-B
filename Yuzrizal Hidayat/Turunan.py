# Mengimpor konstanta 'e' dari modul math
from math import e

# Fungsi untuk menghitung turunan menggunakan metode selisih maju
def forward_difference(y_values, h, index):
    return (y_values[index + 1] - y_values[index]) / h

# Fungsi untuk menghitung turunan menggunakan metode selisih mundur
def backward_difference(y_values, h, index):
    return (y_values[index] - y_values[index - 1]) / h

# Fungsi untuk menghitung turunan menggunakan metode selisih tengah
def central_difference(y_values, h, index):
    return (y_values[index + 1] - y_values[index - 1]) / (2 * h)

# Meminta pengguna memasukkan jumlah titik data
n = int(input("Masukkan jumlah data: "))

# List untuk menyimpan nilai x dan f(x)
x_values = []
y_values = []

# Meminta pengguna memasukkan nilai x dan f(x) untuk setiap titik data
print("Masukkan nilai x dan f(x) untuk setiap titik data:")
for i in range(n):
    x, y = map(float, input().split())
    x_values.append(x)
    y_values.append(y)

# Meminta pengguna memasukkan indeks di mana turunan dihitung dan nilai step size (h)
index = int(input("Masukkan indeks di mana turunan dihitung (indeks dimulai dari 0): "))
h = float(input("Masukkan nilai step size (h): "))

# Menghitung turunan menggunakan metode selisih maju, selisih mundur, dan selisih tengah
turunan_maju = forward_difference(y_values, h, index)
turunan_mundur = backward_difference(y_values, h, index)
turunan_tengah = central_difference(y_values, h, index)

# Menampilkan hasil turunan
print(f"Turunan menggunakan metode selisih maju: {turunan_maju}")
print(f"Turunan menggunakan metode selisih mundur: {turunan_mundur}")
print(f"Turunan menggunakan metode selisih tengah: {turunan_tengah}")
