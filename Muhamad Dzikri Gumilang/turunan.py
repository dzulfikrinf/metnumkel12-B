from math import e

# Fungsi menjalankan turunan dengan metode maju
def forward_difference(y_values, h, index):
    return (y_values[index + 1] - y_values[index]) / h

# Fungsi menjalankan turunan dengan metode mundur
def backward_difference(y_values, h, index):
    return (y_values[index] - y_values[index - 1]) / h

# Fungsi menjalankan turunan dengan metode selisih tengah
def central_difference(y_values, h, index):
    return (y_values[index + 1] - y_values[index - 1]) / (2 * h)

# Input nilai x dan f(x)
n = int(input("Masukkan jumlah baris data: "))
x_values = []
y_values = []

print("Masukkan nilai x dan f(x) pada setiap baris:")
for i in range(n):
    x, y = map(float, input().split())
    x_values.append(x)
    y_values.append(y)

# Input indeks titik (turunan dihitung dan nilai step size (h))
index = int(input("Masukkan indeks titik di mana turunan dihitung (indeks dimulai dari 0): "))
h = float(input("Masukkan nilai step size (h): "))

# Hitung turunan dengan metode maju, mundur, dan selisih tengah
turunan_maju = forward_difference(y_values, h, index)
turunan_mundur = backward_difference(y_values, h, index)
turunan_tengah = central_difference(y_values, h, index)

# Cetak hasil turunan
print(f"Turunan menggunakan metode selisih maju: {turunan_maju}")
print(f"Turunan menggunakan metode selisih mundur: {turunan_mundur}")
print(f"Turunan menggunakan metode selisih tengah: {turunan_tengah}")
