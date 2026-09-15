# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3029 = int(input("Input angka-1: "))
angka2_3029 = int(input("Input angka-2: "))

# Penjumlahan
hasil_3029 = angka1_3029 + angka2_3029
print("\nOperator Penjumlahan")
print("Hasil =",hasil_3029)

# Pengurangan
hasil_3029 = angka1_3029 - angka2_3029
print("\nOperator Pengurangan")
print("Hasil =",hasil_3029)

# Perkalian
hasil_3029 = angka1_3029 * angka2_3029
print("\nOperator Perkalian")
print("Hasil =",hasil_3029)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3029 != 0:
    hasil_3029 = angka1_3029 / angka2_3029
    print("\nOperator Pembagian")
    print("Hasil =",hasil_3029)

    hasil_3029 = angka1_3029 // angka2_3029
    print("\nOperator Pembagian Bulat")
    print("Hasil =",hasil_3029)

    hasil_3029 = angka1_3029 % angka2_3029
    print("\nOperator Sisa Bagi")
    print("Hasil =",hasil_3029)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_3029 = angka1_3029 ** angka2_3029
print("\nOperator Pangkat")
print("Hasil =",hasil_3029)