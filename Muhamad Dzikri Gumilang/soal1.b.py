# untuk mengimpor library math sehingga bisa menggunakan konstanta matematika,
# khusunya disini nilai e (bilangan euler).
import math

# menentukan fungsi f(x) yang akan dicari akarnya.
def f(x): 
    return math.exp(x) - x 

# definisi fungsi bisection yang digunakan untuk mencari akar fungsi dengan metode bagi dua,
# dan menerima 3 parameter yaitu, batas bawah interval (a), batas atas interval (b), serta iterasinya (tol).
def bisection(a, b, tol):
    # Proses mencari akar
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            return c
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

# definisi variabel a dan b yang menunjukkan interval dan ketelitian
# untuk menghitung keakuratan akar yang akan dihitung.
a = -1.0
b = 1.0
ketelitian = 1e-3

# mencari hasil akar fungsi dalam interval yang nantinya disimpan di variabel akar_hampiran,
# dengan memanggil fungsi bisection.
akar_hampiran = bisection(a, b, ketelitian)

# hasil akar yang sudah ditemukan kemudian dicetak ke layar.
print("Akar hampiran:", akar_hampiran)