# deklarasi fungsi interpolasi lagrange
def interpolasi_lagrange(x_data, y_data, nilai_interpolasi):
    n = len(x_data)
    hasil_interpolasi = 0.0
    
    # proses interpolasi
    for i in range(n):
        basis_lagrange = 1.0

        for j in range(n):
            if i != j:
                basis_lagrange *= (nilai_interpolasi - x_data[j]) / (x_data[i] - x_data[j])

        hasil_interpolasi += y_data[i] * basis_lagrange

    return hasil_interpolasi

# Input data dari pengguna
n_data = int(input("Masukkan jumlah pasangan data (n): "))
x_data = []
y_data = []

print("Masukkan pasangan nilai x dan y:")
for i in range(n_data):
    x = float(input(f"Masukkan x{i + 1}: "))
    y = float(input(f"Masukkan y{i + 1}: "))
    x_data.append(x)
    y_data.append(y)

# Input nilai untuk diinterpolasi
nilai_interpolasi = float(input("Masukkan nilai x untuk diinterpolasi: "))

# Menghitung hasil interpolasi Lagrange menggunakan fungsi interpolasi_lagrange
hasil_interpolasi = interpolasi_lagrange(x_data, y_data, nilai_interpolasi)

# Menampilkan hasil interpolasi
print(f"Hasil interpolasi Lagrange pada x = {nilai_interpolasi} adalah {hasil_interpolasi}")
