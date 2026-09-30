# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3029 = int(input("Masukkan nilai batas: "))
for i_3029 in range(batas_3029 + 1):
    for j_3029 in range(batas_3029 + 1):
        print(i_3029+j_3029,end=" ")
    print() # pindah ke baris berikutnya