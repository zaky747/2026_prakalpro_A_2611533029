# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("======================================")
print("1. OPERATOR KEANGGOTAAN")
print("======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3029 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3029 = [int(angka.strip() for angka in input_data_3029.split(','))]

nilai_dicari_3029 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3029 = nilai_dicari_3029 in data_3029
print("\nOperator keanggotaan IN")
print(nilai_dicari_3029,"in",data_3029,"=",hasil_3029)

# Operator not in
hasil_3029 = nilai_dicari_3029 not in data_3029
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3029,"not in",data_3029,"=",hasil_3029)

print("======================================")
print("2. OPERATOR IDENTIAS")
print("======================================")

# objek1 menggunakan list dari input perngguna
object1_3029 = data_3029

# objek2 merujuk pada objek yang sama dengan objek1
object2_3029 = object1_3029

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_3029 = data_3029.copy()

print("object1 =",object1_3029)
print("object2 =",object2_3029)
print("object3 =",object3_3029)

# Operator is
hasil_3029 = object1_3029 is object2_3029
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_3029)

# Operator is not
hasil_3029 = object1_3029 is not object2_3029
print("\nOperator identitas IS NOT")
print("objek1 is not objek2 =",hasil_3029)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_3029 is object3_3029)
print("objek1 == objek3 =",object1_3029 == object3_3029)