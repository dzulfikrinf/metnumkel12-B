import numpy as np

# Fungsi untuk proses eliminasi gauss jordan
def gauss_jordan_elimination(A, b):
    n = len(A)
    augmented_matrix = np.column_stack((A, b))

    for i in range(n):
        max_index = np.argmax(abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_index]] = augmented_matrix[[max_index, i]]

        diagonal_element = augmented_matrix[i, i]
        augmented_matrix[i] /= diagonal_element

        for j in range(n):
            if i != j:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # Ambil matriks hasil setelah eliminasi
    solution = augmented_matrix[:, n:]

    return solution

# Fungsi untuk input matriks dari pengguna
def input_matrix():
    n = int(input("Masukkan ukuran matriks (n x n): "))
    print("Masukkan elemen matriks baris per baris:")
    matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix

# Fungsi untuk input vektor b dari pengguna
def input_vector_b(n):
    print("Masukkan elemen vektor b:")
    b = list(map(float, input().split()))
    if len(b) != n:
        print("Jumlah elemen vektor b harus sama dengan ukuran matriks.")
        return input_vector_b(n)
    return b

# Input matriks dari pengguna
matrix = input_matrix()

# Input vektor b dari pengguna
vector_b = input_vector_b(len(matrix))

# Menyelesaikan sistem persamaan linear dengan metode gauss jordan
solution = gauss_jordan_elimination(matrix, vector_b)

# Menampilkan solusi
print("\nSolusi dari sistem persamaan linear:")
print(solution)
