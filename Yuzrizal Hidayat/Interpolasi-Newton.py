def interpolasi_newton(x_data, y_data, nilai_interpolasi):
    n = len(x_data)

    # Menghitung tabel beda terbagi
    tabel_beda = [[0] * n for _ in range(n)]
    for i in range(n):
        tabel_beda[i][0] = y_data[i]

    # Iterasi untuk mengisi tabel beda terbagi
    for j in range(1, n):
        for i in range(n - j):
            tabel_beda[i][j] = (tabel_beda[i + 1][j - 1] - tabel_beda[i][j - 1]) / (x_data[i + j] - x_data[i])

    # Menghitung hasil interpolasi Newton
    hasil_interpolasi = tabel_beda[0][0]
    for j in range(1, n):
        suku = 1
        for i in range(j):
            suku *= (nilai_interpolasi - x_data[i])
        hasil_interpolasi += tabel_beda[0][j] * suku

    return hasil_interpolasi

# Input data dari pengguna
n_data = int(input("Masukkan jumlah pasangan data (n): "))
x_data = []
y_data = []

# Input pasangan nilai x dan y dari pengguna
print("Masukkan pasangan nilai x dan y:")
for i in range(n_data):
    x = float(input(f"Masukkan x{i + 1}: "))
    y = float(input(f"Masukkan y{i + 1}: "))
    x_data.append(x)
    y_data.append(y)

# Input nilai x yang ingin diinterpolasi
nilai_interpolasi = float(input("Masukkan nilai x untuk diinterpolasi: "))

# Menghitung hasil interpolasi Newton menggunakan fungsi interpolasi_newton
hasil_interpolasi = interpolasi_newton(x_data, y_data, nilai_interpolasi)

# Menampilkan hasil interpolasi
print(f"Hasil interpolasi Newton pada x = {nilai_interpolasi} adalah {hasil_interpolasi}")
