# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_3029 = int(input("Input angka-1: "))
angka2_3029 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =",angka1_3029)
print("Nilai angka2 =",angka2_3029)

# Assigment biasa
hasil_3029 = angka1_3029 
print("\nAssigment biasa (=)")
print("Hasil =",hasil_3029)

# Assigment penambahan
hasil_3029 = angka1_3029 
hasil_3029 += angka2_3029 
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_3029)

# Assigment pengurangan
hasil_3029 = angka1_3029 
hasil_3029 -= angka2_3029 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_3029)

# Assigment perkalian
hasil_3029 = angka1_3029 
hasil_3029 *= angka2_3029
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_3029)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_3029 != 0:
    hasil_3029 = angka1_3029 
    hasil_3029 /= angka2_3029
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_3029)
    # Operator tambahan
    hasil_3029 = angka1_3029 
    hasil_3029 //= angka2_3029
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_3029)
    hasil_3029 = angka1_3029 
    hasil_3029 %= angka2_3029
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_3029)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_3029 = angka1_3029 
hasil_3029 **= angka2_3029
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_3029)