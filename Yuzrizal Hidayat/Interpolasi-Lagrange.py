def interpolasi_lagrange(x_data, y_data, nilai_interpolasi):
    # Mendapatkan jumlah pasangan data
    n = len(x_data)
    
    # Inisialisasi nilai hasil interpolasi
    hasil_interpolasi = 0.0

    # Iterasi untuk setiap titik interpolasi
    for i in range(n):
        # Inisialisasi nilai basis Lagrange untuk titik interpolasi saat ini
        basis_lagrange = 1.0

        # Iterasi untuk setiap titik data
        for j in range(n):
            if i != j:
                # Menghitung basis Lagrange
                basis_lagrange *= (nilai_interpolasi - x_data[j]) / (x_data[i] - x_data[j])

        # Menambahkan kontribusi dari titik data ke hasil interpolasi
        hasil_interpolasi += y_data[i] * basis_lagrange

    return hasil_interpolasi

# Input jumlah pasangan data dari pengguna
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

# Menghitung hasil interpolasi Lagrange menggunakan fungsi interpolasi_lagrange
hasil_interpolasi = interpolasi_lagrange(x_data, y_data, nilai_interpolasi)

# Menampilkan hasil interpolasi
print(f"Hasil interpolasi Lagrange pada x = {nilai_interpolasi} adalah {hasil_interpolasi}")
