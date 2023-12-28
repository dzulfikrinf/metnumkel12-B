import numpy as np

# Fungsi untuk melakukan dekomposisi LU pada matriks A
def LU_dekomposisi(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Perulangan untuk dekomposisi LU
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j]
            for k in range(i):
                U[i, j] -= L[i, k] * U[k, j]
        for j in range(i + 1, n):
            L[j, i] = A[j, i]
            for k in range(i):
                L[j, i] -= L[j, k] * U[k, i]
            L[j, i] /= U[i, i]

    return L, U

# Fungsi untuk menyelesaikan sistem persamaan linear menggunakan dekomposisi LU
def selesaikan_LU(L, U, b):
    n = len(b)
    y = np.zeros(n)  # Matriks untuk menyimpan nilai y
    x = np.zeros(n)  # Matriks untuk menyimpan nilai x

    # Substitusi maju untuk mencari nilai y
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

    # Substitusi mundur untuk mencari nilai x
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x, y

# Input ordo matriks A, tergantung pada jumlah persamaan
n = int(input("Masukkan ordo matriks A: "))
A = np.zeros((n, n))
b = np.zeros(n)

# Input elemen-elemen matriks A dan vektor b
print("Masukkan elemen matriks A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))

print("Masukkan elemen vektor b:")
for i in range(n):
    b[i] = float(input(f"b[{i+1}]: "))

L, U = LU_dekomposisi(A)

# Cetak matriks L
print("Matriks L:")
for i in range(n):
    for j in range(n):
        print(L[i, j], end="\t")
    print()

# Cetak matriks U
print("Matriks U:")
for i in range(n):
    for j in range(n):
        print(U[i, j], end="\t")
    print()

x, y = selesaikan_LU(L, U, b)

# Cetak nilai y
print("Nilai y:")
print(y)

# Cetak solusi x
print("Solusi x:")
print(x)
