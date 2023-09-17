def f(x):
    return x**3 - 2*x + 1 # Mendefinisikan fungsi soal

# Mendefinisikan fungsi untuk mencari akar menggunakan metode bagi dua 
def bisection(a, b, tlt): 
    # Proses mencari akar
    while (b - a) / 2.0 > tlt:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            return c
        elif f(a) * f(c) < 0.0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

# definisi interval awal [a, b] dan ketelitian
a = -1.0
b = 1.0
ketelitian = 1e-3

# Memanggil fungsi metode bagi dua untuk mencari akar
akar_hampiran = bisection(a, b, ketelitian)

print("Akar hampiran:", akar_hampiran) # Hasil akar
