# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3029 = int(input("Masukkan nilai batas: "))
for line_3029 in range(1,batas_3029 + 1):
    for j_3029 in range(1,(-1 * line_3029 + batas_3029) + 1):
        print(".",end="")
    print(line_3029)