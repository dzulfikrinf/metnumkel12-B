import math # untuk mengimpor library math sehingga bisa menggunakan konstanta matematika, khusunya disini nilai e (bilangan euler).
import numpy as np # untuk mengimpor numpy agar bisa melakukan operasi matematika (perhitungan numerik).
import matplotlib.pyplot as plt # untuk mengimpor matplotlib.pyplot agar bisa membuat dan menampilkan grafik.

# menentukan fungsi f(x) yang akan dicari akarnya.
def f(x):
    return eval(persamaan)

# definisi fungsi bisection yang digunakan untuk mencari akar fungsi dengan metode bagi dua.
def bisection(a, b, tlt, n):
    iterasi = []
    for i in range(n):
        c = (a + b) / 2.0
        iterasi.append(c)
        if f(c) == 0.0 or (b - a) / 2.0 < tlt:
            return c, iterasi
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0, iterasi

# Masukan persamaan fungsi f(x), batas interval, jumlah maksimum iterasi, dan keakuratan angka dibelakang koma.
persamaan = input("Masukkan persamaan fungsi (contoh: 'x**2 - 2*x - 8'): ")

# mengganti e (bilangan euler) dengan math.e dalam persamaan sehingga nilai e bisa digunakan.
persamaan = persamaan.replace("e", "math.e")

a = float(input("Masukkan batas bawah interval (a): "))
b = float(input("Masukkan batas atas interval (b): "))
n = int(input("Masukkan jumlah maksimum iterasi: "))
teliti = float(input("Masukkan ketelitian (contoh : '0.001', 3 angka dibelakang koma): "))

# mencari hasil akar fungsi dalam interval yang nantinya disimpan di variabel akar_hampiran,
# dengan memanggil fungsi bisection.
akar_hampiran, iterasi = bisection(a, b, teliti, n)

# untuk membuat grafik fungsi yang akan ditampilkan dengan menggunakan array x dan y.
x = np.linspace(a, b, 400)
y = [f(xi) for xi in x]

# mengambil nilai x dari iterasi untuk ditampilkan di grafik.
iterasi_x = [a, b] + iterasi

# menampilkan grafik fungsi dan iterasi yang sudah dilakukan.
plt.plot(x, y, label=f'f(x) = {persamaan}')
plt.axhline(0, color='red', linestyle='--', linewidth=0.7, label='y = 0')
plt.scatter(iterasi_x, [f(xi) for xi in iterasi_x], color='green', label='Iterasi', zorder=5)
plt.annotate(f'Akar hampiran: {akar_hampiran:.6f}', (akar_hampiran, f(akar_hampiran)), color='blue')

# membangun grafik.
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik fungsi f(x) dengan Iterasi Metode Biseksi')
plt.grid(True)
plt.legend()

# mencetak grafik kepada user.
plt.show()